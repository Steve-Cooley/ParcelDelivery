from Parcel import Parcel

class MyHashmapClass:

    # This constructor determines how large the empty hash table will be.  I want to reduce collisions for
    # performance reasons, so I multiply the table size by 10.  This will grow with the business as long as
    # the user of this program enters in the number of packages to be delivered.
    def __init__(self, number_of_packages: int = 10):
        self.inventory = []
        # This list of keys is part of an attempt to make iterating through the hashmap easier
        self.key_list = []
        self.inventory_capacity = number_of_packages * 10

        for i in range(self.inventory_capacity):
            self.inventory.append([])

    # Changes the print output to something more useful than the v-memory address of the hashmap.
    # It just prints the list of "inventory"
    # For now, this doesn't use the print __str__ method of the internal parcel objects, might change later fixme
    def __str__(self):
        print('in hashtable __str__ method')
        return self.inventory.__str__()

    ## insert method
    def insert(self, parcel: Parcel):
        #print("in insert method") #fixme remove
        # get ID, and hash it to determine bucket
        id = parcel.get_id()
        bucket  = hash(id) % self.inventory_capacity
        #print('bucket is: ' + str(bucket))
        self.inventory[bucket].append(parcel)
        self.key_list.append(id)

    ## search method
    # Complexity: Worst case is O(n), but in reality it's more like O(1) because hash collisions should be rare.
    # So, runtime will be something like O(n / (inventory_capacity?)) fixme
    def search(self, id: str):
        print('in hm search method') # fixme delete
        bucket_int = hash(id) % self.inventory_capacity
        actual_bucket = self.inventory[bucket_int]
        print("********* Length of bucket: " + str(len(actual_bucket)))
        for par in actual_bucket:
            return par

    ## remove method  fixme delete?

    # this method should mark parcels ready or not ready depending on a number of criteria based on criteria
    # What parcels share addresses?
    # what parcels are chained together in some other way
    # what parcels that share an address or are otherwise chained  together that have a high priority?
    def optimize_parcels(self):
        pass

    # get list of available loaded_parcels.
    def get_ready_parcels(self):
        self.optimize_parcels()
        ready_parcels = []
        for key in self.key_list:
            bucket = hash(key) % self.inventory_capacity
            #print(bucket) #prints a list of active bucket numbers
            #print(self.inventory[bucket]) # this prints a list of the contents of each active bucket, which are lists
            for par in self.inventory[bucket]:
                #print(par)
                #print (par.get_status())
                if par.get_status() == 'waiting':
                    ready_parcels.append(par)
        return ready_parcels

    def print_all_parcels(self):
        print("*********printing all loaded_parcels**************")
        for key in self.key_list:
            bucket = hash(key) % self.inventory_capacity
            for par in self.inventory[bucket]:
                print(par)

