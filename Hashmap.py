from Parcel import Parcel

class Hashmap:

    # This constructor determines how large the empty hash table will be.  I want to minimize collisions for
    # performance reasons, so I multiply the table size by 10.  This will grow with the business as long as
    # the user of this program enters in the number of packages to be delivered.
    def __init__(self, number_of_packages: int = 10):
        self.inventory = []
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
        bucket  = hash(parcel.get_id()) % self.inventory_capacity
        #print('bucket is: ' + str(bucket))
        self.inventory[bucket].append(parcel)

    ## search method
    # I apparently needed to verify that the object inside of the bucket that I'm indexing is in fact a parcel
    # Before I could access it's methods. Not sure if this was just some kind of mistake, but I think it works.
    # Complexity: Worst case is O(n), but in reality it's more like O(1) because hash collisions should be rare.
    def search(self, id: str):
        print('in hm search method') # fixme delete
        bucket_int = hash(id) % self.inventory_capacity
        actual_bucket = self.inventory[bucket_int]
        print("********* Length of bucket: " + str(len(actual_bucket)))
        for i in range(len(actual_bucket)):
            if type(actual_bucket[i]) is Parcel:
                print("In hm.  Yes, is parcel!")  # fixme delete
                return actual_bucket[i]


    ## remove method