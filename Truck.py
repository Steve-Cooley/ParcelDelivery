
#class "delivers" parcels.  It can hold only 16 parcels at a time.
class Truck:
    print("@@@@@@@@@@@@@Truck class is running for some reason.")
    def __init__(self):
        self.slots = 16

    def load_truck(self):
        print()
        parcels = []

