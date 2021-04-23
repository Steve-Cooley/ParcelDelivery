# This project by:  Steven Cooley   __id# 001009672
from datetime import datetime

import truck
from data import load_parcels
from hash_module import MyHashmapClass


# time: O(n^2) space: O(n^2) This function calls on other methods and functions in other modules,
# and if you follow the logic through each method/function, I expect that you'd find O(n^[5,9]).
# This is still polynomial time.
# Runs trucks via a while loop limited to ten trips per truck. This limitation was useful early on.
# Trucks are alternated to simulate simultaneity between trucks.  UI loop implemented to make
# repeated runs easier.
def main():
    short_hashy = MyHashmapClass(40)
    load_parcels(short_hashy)
    print()
    print("**************** Running with termination time ******************")
    # Allow user to enter a stop time so they can check on the status of all packages at that time.
    print("Enter a time below. Once you enter a time, the program will run once, and show the\n"
          "status of all packages (parcels) at that time. Packages that have been\n"
          "delivered on time will have a timestamp. Likewise if any packages are late,\n"
          "they'll have a message stating that they are late, and a timestamp (all \n"
          "packages are always delivered on time though for this version of this\n"
          "program). If stopped early (by the time you enter), some packages will say that they\n"
          "'waiting', loaded on a truck, or delayed for some reason.The program will run on\n"
          "repeat until you press 'n' when prompted.\n")
    answer = 'y'
    # loop intended to make running the program with different inputs easier.
    while not answer == 'n':
        short_hashy = MyHashmapClass(40)
        load_parcels(short_hashy)
        utime = input("Enter a time in military time in the format HH:MM\n_")
        utime = datetime.strptime(utime, "%H:%M")
        tr1 = truck.Truck(1, short_hashy)
        tr2 = truck.Truck(2, short_hashy)
        tr1_total_distance = 0
        tr2_total_distance = 0
        # loop alternates truck runs. Limiting number of runs was useful early in the dev process.
        # It turns out that running and loading truck 2 before truck 1 gave a shorter path that
        # met all requirements.
        i = 9
        while len(short_hashy.get_ready_parcels()) > 0 and (i > 0):
            tr2_total_distance = tr2.run_route(short_hashy, utime)
            tr1_total_distance = tr1.run_route(short_hashy, utime)
            i = i - 1
        short_hashy.print_all_parcels()
        total_distance = tr1_total_distance + tr2_total_distance
        print("\n*************** Final report *****************")
        print("Truck 1 mileage = {:.3f}, truck 2 mileage = {:.3f} total = {:.3f}".format(tr1_total_distance,
                                                                                         tr2_total_distance,
                                                                                         total_distance))
        answer = input("Enter 'n' to quit.  This program will keep re-running until you enter 'n': ")



main()
