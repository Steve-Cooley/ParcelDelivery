from Parcel import Parcel


# This self-adjusting data structure holds all of the parcel objects. The most expensive
# method is O(n^2) (time complexity). This data structure makes a lot of empty lists
# in order to speed up access time at the expense of some space complexity.
class MyHashmapClass:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Constructor creates the hashmap.
    def __init__(self, number_of_packages: int = 40):
        self.inventory = []
        # This list of keys (IDs) is part of an attempt to make iterating through the hashmap easier
        self.key_list = []
        self.inventory_capacity = number_of_packages * 100
        self.truck_turn = 1  # selects which truck is active.  Not sure if this will be used fixme
        # This makes the algorithm self adjusting, responding to the number of packages inserted
        for i in range(self.inventory_capacity):
            self.inventory.append([])

    # time: O(1)
    # space: O(1)
    # Returns string of object
    def __str__(self):
        print('in hashtable __str__ method')
        return self.inventory.__str__()

    # space: O(1)
    # time: O(1)
    # insert method inserts parcels into hashtable using hash function.
    def insert(self, parcel: Parcel):
        # get ID, and hash it to determine bucket
        id = parcel.get_id()
        bucket = hash(id) % self.inventory_capacity
        self.inventory[bucket].append(parcel)
        self.key_list.append(id)

    # time: O(n) space: O(n)
    # search method takes an id number as an argument and uses the hash function to return
    # a parcel object.
    def search(self, id: str):
        bucket_int = hash(id) % self.inventory_capacity
        actual_bucket = self.inventory[bucket_int]
        for par in actual_bucket:
            return par

    # time: O(n^2) space: O(n^2)
    # get list of available loaded_parcels.
    def get_ready_parcels(self):
        ready_parcels = []
        for key in self.key_list:
            bucket = hash(key) % self.inventory_capacity
            for par in self.inventory[bucket]:
                if (par.get_status() == 'waiting') and par.get_id() == key:
                    ready_parcels.append(par)
                    # print(par)
        return ready_parcels

    # space: O(n^2) time: O(n^2)
    def print_all_parcels(self):
        print("*********printing all loaded_parcels**************")
        key01 = hash('01') % self.inventory_capacity
        for key in self.key_list:
            bucket = hash(key) % self.inventory_capacity
            for par in self.inventory[bucket]:
                print(par)