# This project by:  Steven Cooley   __id# 001009672
from Parcel import Parcel
from Hashmap import Hashmap
from data import load_parcels
from data import get_address_index
from datetime import datetime
from data import get_distance_between_addresses

class TemporaryClass:
    def __init__(self):
        self.__myString = "Hello, World!"
    def __str__(self):
        return self.__myString


def test():
    tc = TemporaryClass()

    print("testing")

    print(tc)

    pack00 = Parcel('1',
                   '123 address',
                   "22 00",
                   "city1",
                   'zip1',
                   '1.3#',
                   )
    print(pack00)
    print('pack hash: ' + str(hash(pack00)))
    pack00.setStatusEnRoute()
    print('status has been set to en route')
    print(pack00)
    print('pack hash: ' + str(hash(pack00)))
    print('Hash of string matching package number: ' + str(hash('1')))
    pack00.id = '2'
    print('Hash of package after changing the parcel number: ' + str(hash(pack00)))

    print('***********')
    print('Now testing hashmap')
    hashy = Hashmap(40)
    # print(hashy)
    # hashy.insert(pack00)
    # print(hashy)
    # pack01 = Parcel('2', 'address2', '00 00', 'city2', 'zip2', 'weight2')
    # pack02 = Parcel('3', 'address3', '00 00', 'city3', 'zip3', 'weight3')
    # hashy.insert(pack01)
    # hashy.insert(pack02)

    print(hashy)

    print('************ now testing loader ***************')
    #hashy = load_parcels(hashy)
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

def main():
    test()


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