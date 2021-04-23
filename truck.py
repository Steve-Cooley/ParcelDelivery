from datetime import datetime, timedelta

import Parcel
import data
from hash_module import MyHashmapClass


# class "delivers" loaded_parcels.  It can hold only 16 loaded_parcels at a time.
# Keeps track of miles traveled and other relevant data.
class Truck:
    # time: O(1) space O(1)
    # Basic constructor, initiates all members.
    def __init__(self, truck_number, hashy: MyHashmapClass):
        self.open_slots = 16
        self.loaded_parcels = []
        self.miles_traveled = 0
        self.truck_number = truck_number
        self.time = datetime.strptime('8 00', '%H %M')
        # converted 18 miles per hour to miles per minute (18/60)
        self.TRUCK_SPEED = 0.3
        self.current_location = 'HUB'
        self.hashy = hashy
        self.stop_all = False

    # time: O(n) space: O(n).  There are several loops here, but no nested loops.
    # This loads the truck based on priority.
    def load_truck(self, hm: MyHashmapClass):
        ready_parcels = hm.get_ready_parcels()
        # remove incompatible parcels
        compat_parcels = []
        for par in ready_parcels:
            if par.get_required_truck() == self.truck_number or par.get_required_truck() == -1:
                compat_parcels.append(par)
        ready_parcels = compat_parcels
        # find priority parcels
        temp_priororitized_parcels = []
        #   priority 0
        for par in ready_parcels:
            pri = par.get_priority()
            if pri == 0:
                temp_priororitized_parcels.append(par)
        #   priority 1
        for par in ready_parcels:
            pri = par.get_priority()
            if pri == 1:
                temp_priororitized_parcels.append(par)
        # remove all higher prioritized packages from main list
        for par in temp_priororitized_parcels:
            ready_parcels.remove(par)
        # concatenate lists, creating new list with higher priority packages at the front
        ready_parcels = temp_priororitized_parcels + ready_parcels
        # prevent OOB errors:
        num_ready_parcels = len(ready_parcels)
        if num_ready_parcels < self.open_slots:
            self.open_slots = num_ready_parcels
        # Actually load the parcels onto the truck
        for i in range(self.open_slots):
            par = ready_parcels[i]
            self.loaded_parcels.append(par)
            self.open_slots = self.open_slots - 1
        #   change the status of loaded parcels to reflect the truck they are on
        for par in self.loaded_parcels:
            par.set_status_on_truck(self.truck_number)

    # time: O(1) space: O(1)
    # This method "delivers" parcels by changing their status.  If a package is late, it will reflect
    # that. Uses a timestamp to inform the user of the time it was delivered.
    def deliver_parcel(self, par: Parcel):
        if self.time > par.get_deadline():
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!parcel {} delivered late at {}".format(par.get_id(), self.time))
            par.set_status_late(self.time)
        else:
            par.set_status_delivered(self.time)
        # remove from truck
        self.loaded_parcels.remove(par)
        self.open_slots = self.open_slots + 1

    # time: O(n) space: O(n)  Although there are multiple loops, none are nested.  It does call on other
    # methods that have their own loops, so I think in some cases you get up to O(n^3) if you look a little
    # deeper.
    # This method actually runs the truck, calling on other methods that load the truck, go to a new
    # location, deliver parcels, etc.  It's divided into several loops to help with prioritizing different
    # packages.
    def run_route(self, hashy: MyHashmapClass, stop_time: datetime = datetime.strptime("22:00", "%H:%M")):
        # This loop ensures that the route is only run if time isn't up (time is set by user/evaluator)
        if self.stop_all == True or self.time >= stop_time:
            #breaks the loop if there is no need to run (because the user entered a certain time)
            return self.miles_traveled
        else:
            # Determine if the route should run, are there any packages in hashy?
            num_ready_parcels = len(hashy.get_ready_parcels())
            self.load_truck(hashy)
            # deliver priority 0 parcels
            pri_0_parcels = []
            for par in self.loaded_parcels:
                if par.get_priority() == 0:
                    pri_0_parcels.append(par)
            while len(pri_0_parcels) > 0:
                par = self.get_nearest_package(pri_0_parcels)
                delivery_address = par.get_d_address()
                self.go_to_next_location(delivery_address)
                self.deliver_parcel(par)
                pri_0_parcels.remove(par)
                # enable stop time
                if self.time >= stop_time:
                    self.stop_all = True
                    return self.miles_traveled
            # deliver priority 1 parcels
            pri_1_parcels = []
            for par in self.loaded_parcels:
                if par.get_priority() == 1:
                    pri_1_parcels.append(par)
            while len(pri_1_parcels) > 0:
                par = self.get_nearest_package(pri_1_parcels)
                delivery_address = par.get_d_address()
                self.go_to_next_location(delivery_address)
                self.deliver_parcel(par)
                pri_1_parcels.remove(par)
                if self.time >= stop_time:
                    self.stop_all = True
                    return self.miles_traveled
            # The main loop that runs until all loaded parcels have been delivered or returned to hub
            while len(self.loaded_parcels) > 0:
                par = self.get_nearest_package(self.loaded_parcels)
                delivery_address = par.get_d_address()
                self.go_to_next_location(delivery_address)
                self.deliver_parcel(par)
                self.new_arrivals_round1()
                self.new_arrivals_round2()
                if self.time >= stop_time:
                    self.stop_all = True
                    return self.miles_traveled
            length_of_parcels = len(self.loaded_parcels)
            # return to HUB
            self.return_to_hub()
            return self.miles_traveled

    # time: O(1) space: O(1)
    # This method checks for packages that have become available after the truck has departed. This was
    # necessary because some packages that became available for delivery after the start of business
    # are also high priority.
    def new_arrivals_round1(self):
        par6 = self.hashy.search('06')
        if (self.time > datetime.strptime("09 05", "%H %M")) and (par6.get_status() == 'delayed'):
            par6.set_status_waiting()
            par6.set_required_truck(self.truck_number)
            self.hashy.search('25').set_status_waiting()
            self.hashy.search('25').set_required_truck(self.truck_number)
            self.hashy.search('26').set_status_waiting()
            self.hashy.search('26').set_required_truck(self.truck_number)
            self.hashy.search('28').set_status_waiting()
            self.hashy.search('28').set_required_truck(self.truck_number)
            self.hashy.search('32').set_status_waiting()
            self.hashy.search('32').set_required_truck(self.truck_number)
            self.return_to_hub()

    # time: O(1) space: O(1)
    # This method checks for packages that have become available after the truck has departed. This was
    # necessary because some packages that became available for delivery after the start of business
    # are also high priority.
    def new_arrivals_round2(self):
        par9 = self.hashy.search('09')
        if (self.time > datetime.strptime("10 20", "%H %M")) and (par9.get_status() == 'delayed until 1020'):
            par9.set_status_waiting()
            par9.set_d_address('410 S State St')
            par9.set_required_truck(self.truck_number)
            self.return_to_hub()

    # time: O(1) space: O(1)
    # "Moves" the truck from one location to another.
    def go_to_next_location(self, next_address: str):
        # calculate distance to next location, add that to accumulator, update current_location
        distance = data.get_distance_between_addresses(self.current_location, next_address)
        self.current_location = next_address
        self.miles_traveled = self.miles_traveled + distance
        # add to time: t=d/r
        time_added = distance / self.TRUCK_SPEED
        self.time = self.time + timedelta(minutes = time_added)


    # time: O(n) space: O(n)
    # This returns the vehicle to the HUB. If the truck is loaded, it unloads it.
    # This was necessary to ensure that there was room on the truck for high
    # priority packages on future runs. Because this uses the method
    # "go_to_next_location", it does add to the mileage of the vehicle.  This
    # method is run at the end of each each run, as long as that run completes.
    # (as opposed to being interrupted by a time entered by the user/evaluator)
    def return_to_hub(self):
        self.go_to_next_location("HUB")
        # unload truck
        ## change status of any loaded parcels to ready
        if len(self.loaded_parcels) > 0:
            for par in self.loaded_parcels:
                par.set_status_waiting()
        ## reset openslots to 16
        self.open_slots = 16
        ## make self.parcels = []
        self.loaded_parcels = []

    # time: O(n) space: O(n)
    # This small method is one of the core elements of the project.  It helps
    # optimize package delivery by finding the package with the nearest
    # delivery address.  It takes a list of parcels, and returns the parcel that
    # has the nearest address.
    def get_nearest_package(self, parcels):
        shortest_distance = 1_000
        closest_address = 'bad address in get nearest package'
        address_list = []
        for par in parcels:
            address = par.get_d_address()
            address_list.append(address)
        # find closest address
        for address in address_list:
            distance = data.get_distance_between_addresses(self.current_location, address)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_address = address
        # return any parcel that has that has that closest address
        for par in parcels:
            address = par.get_d_address()
            if address == closest_address:
                return par

