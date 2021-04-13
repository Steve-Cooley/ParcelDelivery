import Parcel
import data
from hashmap_module import MyHashmapClass
from datetime import datetime, timedelta

# class "delivers" loaded_parcels.  It can hold only 16 loaded_parcels at a time.
# must keep track of miles traveled
import hashmap_module
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

    # O(n)
    def load_truck(self, hm: MyHashmapClass):
        #current_index = 0
        print("loading truck {}".format(self.truck_number))
        ready_parcels = hm.get_ready_parcels()
        number_of_ready_parcels = len(ready_parcels)
        print("number of ready parcels: {}".format(number_of_ready_parcels))
        for i in range(self.open_slots):
            self.loaded_parcels.append(ready_parcels[i])
            self.open_slots = self.open_slots - 1
        num_loaded_parcels = len(self.loaded_parcels)
        print("Number of loaded parcels: {}".format(num_loaded_parcels))
        # change each loaded parcel's status
        for par in self.loaded_parcels:
            par.set_status_on_truck(self.truck_number)
        # check that local package statuses have changed (should also affect hashmap, should be checked)
        for par in ready_parcels:
            print(par)
        # Check that everyhing changed in hashmap:
        #hm.print_all_parcels()
        print("Number of open slots after loading truck: {}".format(self.open_slots))

    # This should deliver all loaded_parcels loaded in truck  whose delivery address
    # matches the current address.  I don't think it technically does this yet, it's
    # kind of working by accident, so need to fix it.  todo
    # Should this take a list instead?  then it could deliver all parcels with the same address. todo
    def deliver_parcel(self, par: Parcel):
        print('delivering parcel(s) to {}'.format(par.get_d_address()))
        par.set_status_delivered(self.time)
        status = par.get_status()
        print(status)
        # remove from truck
        self.loaded_parcels.remove(par)

    # # first draft.  Will need to implement a lot more logic here.
    def run_route(self, hashy: MyHashmapClass):
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
        self.load_truck(hashy)
        print("Loaded parcels: {}".format(self.loaded_parcels))

    def go_to_next_location(self, next_address: str):
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
        print("current time is: ", self.time)


    def return_to_hub(self):
        print("returning to hub")
        self.go_to_next_location("HUB")



