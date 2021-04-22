import Parcel
import data
from hash_module import MyHashmapClass
from datetime import datetime, timedelta

# class "delivers" loaded_parcels.  It can hold only 16 loaded_parcels at a time.
# must keep track of miles traveled
import hash_module
class Truck:
    # O(1)
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


    def load_truck(self, hm: Parcel):
        print("@@@@loading truck {}".format(self.truck_number))
        ready_parcels = hm.get_ready_parcels()
        # remove incompatible parcels
        compat_parcels = []
        for par in ready_parcels:
            if par.get_required_truck() == self.truck_number or par.get_required_truck() == -1:
                compat_parcels.append(par)
        ready_parcels = compat_parcels
        #print(ready_parcels)
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


    # This should deliver all loaded_parcels loaded in truck  whose delivery address
    # matches the current address.  I don't think it technically does this yet, it's
    # kind of working by accident, so need to fix it.  todo
    # Should this take a list instead?  then it could deliver all parcels with the same address. todo
    def deliver_parcel(self, par: Parcel):
        print('delivering parcel {} to {}'.format(par.get_id(), par.get_d_address()))
        if self.time > par.get_deadline():
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!parcel {} delivered late at {}".format(par.get_id(), self.time))
            par.set_status_late(self.time)
        else:
            print("Parcel {} was on time at {}".format(par.get_id(), self.time))
            par.set_status_delivered(self.time)
        #status = par.get_status()
        #print(status)
        # remove from truck
        self.loaded_parcels.remove(par)
        self.open_slots = self.open_slots + 1
        print("there are {} parcels on the truck". format(16 - self.open_slots))

    def run_route(self, hashy: MyHashmapClass, stop_time: datetime = datetime.strptime("22:00", "%H:%M")):
        # This loop ensures that the route is only run if time isn't up (time is set by user)
        if self.stop_all == True or self.time >= stop_time:
            return self.miles_traveled
        else:
            print("************ Start of run_route ***********")
            print("Time is {}".format(self.time.strftime('%H:%M')))
            #hashy.print_all_parcels()
            # Determine if the route should run, are there any packages in hashy?
            num_ready_parcels = len(hashy.get_ready_parcels())
            print("There are {} parcels ready to go".format(num_ready_parcels))
            self.load_truck(hashy)
            print("loaded {} parcels.".format(len(self.loaded_parcels)))
            # deliver priority 0 parcels
            pri_0_parcels = []
            for par in self.loaded_parcels:
                if par.get_priority() == 0:
                    pri_0_parcels.append(par)
            while len(pri_0_parcels) > 0:
                par = self.get_nearest_package(pri_0_parcels)
                #print("Nearest High Priority parcel: ", par)
                delivery_address = par.get_d_address()
                self.go_to_next_location(delivery_address)
                self.deliver_parcel(par)
                pri_0_parcels.remove(par)
                # enable stop time
                if self.time >= stop_time:
                    print("\n **********Stopping early **********\n")
                    self.stop_all = True
                    return self.miles_traveled
            #print("#########HIGH PRIORITY PARCELS: ", pri_0_parcels)
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
                    print("\n **********Stopping early **********\n")
                    self.stop_all = True
                    return self.miles_traveled
            # The main loop that runs until all loaded parcels have been delivered or returned to hub
            while len(self.loaded_parcels) > 0:
                print("there are {} loaded packages".format(len(self.loaded_parcels)))
                par = self.get_nearest_package(self.loaded_parcels)
                print("nearest package: {}".format(par))
                delivery_address = par.get_d_address()
                self.go_to_next_location(delivery_address)
                self.deliver_parcel(par)
                self.new_arrivals_round1()
                self.new_arrivals_round2()
                if self.time >= stop_time:
                    print("\n **********Stopping early **********\n")
                    self.stop_all = True
                    return self.miles_traveled
            length_of_parcels = len(self.loaded_parcels)
            print("Length of self.loaded_parcels after loop: {}".format(length_of_parcels))
            # return to HUB
            self.return_to_hub()
            print("Miles traveled for this trip: {}".format(self.miles_traveled))
            print("************* end of run_route ************\n")
            return self.miles_traveled

    def new_arrivals_round1(self):
        par6 = self.hashy.search('06')
        if (self.time > datetime.strptime("09 05", "%H %M")) and (par6.get_status() == 'delayed'):
            print(">>>>>>>>>>>>>>>It's now after 9:05, and new packages are ready")
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

    def new_arrivals_round2(self):
        par9 = self.hashy.search('09')
        if (self.time > datetime.strptime("10 20", "%H %M")) and (par9.get_status() == 'delayed until 1020'):
            par9.set_status_waiting()
            par9.set_d_address('410 S State St')
            par9.set_required_truck(self.truck_number)
            self.return_to_hub()

    def go_to_next_location(self, next_address: str):
        if next_address == self.current_location and (not next_address == "HUB"):
            print("I don't need to go anywhere!")
        else:
            print("Going from \"{}\" to: \"{}\"".format(self.current_location, next_address))
        # calculate distance to next location, add that to accumulator, update current_location
        distance = data.get_distance_between_addresses(self.current_location, next_address)
        print("the distance was: {} miles".format(distance))
        self.current_location = next_address
        self.miles_traveled = self.miles_traveled + distance
        # add to time: t=d/r
        time_added = distance / self.TRUCK_SPEED
        self.time = self.time + timedelta(minutes = time_added)
        print("time added: {}".format(time_added))
        #print("current time is: ", self.time)


    def return_to_hub(self):
        print("returning to hub")
        self.go_to_next_location("HUB")
        # unload truck
        ## change status of any loaded parcels to ready
        if len(self.loaded_parcels) > 0:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ truck not empty, unloading it now")
            for par in self.loaded_parcels:
                print("unloading parcel {}".format(par.get_id()))
                par.set_status_waiting()
                print("double checking status of parcel {}: {}".format(par.get_id(), par.get_status()))
        ## reset openslots to 16
        self.open_slots = 16
        ## make self.parcels = []
        self.loaded_parcels = []
        #self.load_truck(self.hashy)
        print("There should be no more parcels on the truck.  The number is: {}".format(16 - self.open_slots))

    def get_nearest_package(self, parcels):
        shortest_distance = 1_000
        closest_address = 'bad address in get nearest package'
        address_list = []
        # for par in parcels:
        #     if par.get_status() == 'truck{}'.format(self.truck_number):
        #         return par
        # get all addresses:
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

