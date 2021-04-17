import Parcel
import data
from hash_module import MyHashmapClass
from datetime import datetime, timedelta

# class "delivers" loaded_parcels.  It can hold only 16 loaded_parcels at a time.
# must keep track of miles traveled
import hash_module
class Truck:
    # O(1)
    def __init__(self, truck_number):
        self.open_slots = 16
        self.loaded_parcels = []
        self.miles_traveled = 0
        self.truck_number = truck_number
        self.time = datetime.strptime('8 00', '%H %M')
        # converted 18 miles per hour to miles per minute (18/60)
        self.TRUCK_SPEED = 0.3
        self.current_location = 'HUB'


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
        par.set_status_delivered(self.time)
        #status = par.get_status()
        #print(status)
        # remove from truck
        self.loaded_parcels.remove(par)
        self.open_slots = self.open_slots + 1

    # # first draft.  Will need to implement a lot more logic here.
    def run_route(self, hashy: MyHashmapClass):
        print("************ Start of run_route***********")
        # First, determine if route should run (are there any ready parcels in the hashmap?)
        num_ready_parcels = len(hashy.get_ready_parcels())
        print("There are {} parcels ready to go".format(num_ready_parcels))
        print('running route')
        self.load_truck(hashy)
        # Need to make a copy of a list before iterating over and removing elements of that list.
        temp_list = self.loaded_parcels[:]
        for par in temp_list:
            #print("length of 'loaded_parcels: {}".format(len(self.loaded_parcels)))
            # get delivery_address of parcel
            delivery_address = par.get_d_address()
            self.go_to_next_location(delivery_address)
            self.deliver_parcel(par)
        length_of_parcels = len(self.loaded_parcels)
        print("Length of self.loaded_parcels after loop: {}".format(length_of_parcels))
        #print("Miles traveled for this trip: {}".format(self.miles_traveled))
        # return to HUB
        self.return_to_hub()
        print("Miles traveled for this trip: {}".format(self.miles_traveled))
        print("Time this trip ended: {}".format(self.time.strftime('%H:%M')))
        #print("Loaded parcels: {}".format(self.loaded_parcels))
        #hashy.print_all_parcels()
        num_ready_parcels = len(hashy.get_ready_parcels())
        print("There are {} parcels ready to go".format(num_ready_parcels))
        print("************* end of run_route************")
        # if num_ready_parcels > 4:
        #     self.run_route(hashy)


    def go_to_next_location(self, next_address: str):
        #print("Going from \"{}\" to: \"{}\"".format(self.current_location, next_address))
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



