# This project by:  Steven Cooley   __id# 001009672
import Truck
import data
from Parcel import Parcel
from hash_module import MyHashmapClass
from data import load_parcels
from data import get_address_index
from datetime import datetime
from data import get_distance_between_addresses
from decimal import *

class TemporaryClass:
    def __init__(self):
        self.__myString = "Hello, World!"
    def __str__(self):
        return self.__myString


def test():
    # tc = TemporaryClass()
    #
    # print("testing")
    #
    # print(tc)
    #
    # pack00 = Parcel('1',
    #                '123 address',
    #                "22 00",
    #                "city1",
    #                'zip1',
    #                '1.3#',
    #                )
    # print(pack00)
    # print('pack hash: ' + str(hash(pack00)))
    # pack00.set_status_on_truck(1)
    # print('status has been set to en route')
    # print(pack00)
    # print('pack hash: ' + str(hash(pack00)))
    # print('Hash of string matching package number: ' + str(hash('1')))
    # pack00.id = '2'
    # print('Hash of package after changing the parcel number: ' + str(hash(pack00)))
    #
    # print('***********')
    # print('Now testing hashmap')
    hashy = MyHashmapClass(40)

    #print(hashy)

    print('************ now testing loader ***************')
    load_parcels(hashy)
    print(hashy)

    pack04 =  hashy.search('09')
    print(pack04)

    ##########################################
    # distance stuff

    var = get_address_index('195 W Oakland Ave')
    print(var)

    distance = get_distance_between_addresses('195 W Oakland Ave', 'HUB') # good
    print(distance)
    distance = get_distance_between_addresses('HUB', '195 W Oakland Ave') #Bad!!! fixed!
    print(distance)
    distance = get_distance_between_addresses('300 State St', '1488 4800 S') # good
    print(distance)
    distance = get_distance_between_addresses('HUB', 'HUB') # works fixme delete
    print(distance)
    distance = get_distance_between_addresses('2010 W 500 S', '3060 Lester St')
    print(distance)
    distance = get_distance_between_addresses('3060 Lester St', '2010 W 500 S')
    print(distance)
    #
    print('********** Testing truck!')
    #hashy.next_available(0)
    #parcel_list = hashy.get_ready_parcels()
    #print(parcel_list)
    tr = Truck.Truck(1)
    print(tr)
    #tr.load_truck(hashy)
    tr.run_route(hashy)
    #hashy.print_all_parcels()


def test_trucks():
    # set up hashmap
    hashy = MyHashmapClass(40)
    load_parcels(hashy)

    # set up trucks:
    tr1 = Truck.Truck(1, hashy)
    tr2 = Truck.Truck(2, hashy)
    tr1_total_distance = 0
    tr2_total_distance = 0
    # for debugging purposes, I'm limiting this to 10 cycles (20 total truck runs).  This can be removed later fixme
    i = 9
    while len(hashy.get_ready_parcels()) > 0 and (i > 0):
        tr2_total_distance = tr2.run_route(hashy)
        tr1_total_distance = tr1.run_route(hashy)
        i = i - 1
    hashy.print_all_parcels()
    total_distance = tr1_total_distance + tr2_total_distance
    print("\n*************** Final report *****************")
    print("Truck 1 mileage = {:.3f}, truck 2 mileage = {:.3f} total = {:.3f}".format(tr1_total_distance,
                                                                         tr2_total_distance,
                                                                         total_distance))

def main():
    test_trucks()
    #test()


main()



'''
dateString = "12 14 1978 0 0 0"
print(dateString)
date_object = datetime.strptime(dateString, '%m %d %Y %H %M %S')

print (date_object)


tbl = []
print (tbl)
for i in range(10):
    tbl.append([])
print(tbl)

'''