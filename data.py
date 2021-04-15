from Parcel import Parcel
from hash_module import MyHashmapClass


def load_parcels(hashmap):
    print('loading data')
    print(hashmap)
    pack01 = Parcel('01',
                    '195 W Oakland Ave',
                    '22 00',
                    'Salt Lake City',
                    '84115',
                    '21')
    pack01.set_priority(1)
    pack02 = Parcel('02',
                    '2530 S 500 E',
                    '22 00',
                    'Salt Lake City',
                    '84106',
                    '44')
    pack03 = Parcel('03',
                    '233 Canyon Rd',
                    '22 00',
                    'Salt Lake City',
                    '84103',
                    '21')
    pack03.set_required_truck(2)
    pack04 = Parcel('04',
                    '380 W 2880 S',
                    '22 00',
                    'Salt Lake City',
                    '84115',
                    '4')
    pack05 = Parcel('05',
                    '410 S State St',
                    '22 00',
                    'Salt Lake City',
                    '84111',
                    '5')
    pack06 = Parcel('06',
                    '3060 Lester St',
                    '10 30',
                    'West Valley City',
                    '84119',
                    '88',
                    'delayed')
    pack06.set_priority(0)
    pack07 = Parcel('07',
                    '1330 2100 S',
                    '22 00',
                    'Salt Lake City',
                    '84106',
                    '8')
    pack08 = Parcel('08',
                    '300 State St',
                    '22 00',
                    'Salt Lake City',
                    '84103',
                    '9')
    # Next package has bad address
    pack09 = Parcel('09',
                    '300 State St',
                    '22 00',
                    'Salt Lake City',
                    '84103',
                    '2',
                    'delayed until 1020')  # status set
    pack10 = Parcel('10',
                    '600 E 900 South',
                    '22 00',
                    'Salt Lake City',
                    '84105',
                    '1')
    pack11 = Parcel('11',
                    '2600 Taylorsville Blvd',
                    '22 00',
                    'Salt Lake City',
                    '84118',
                    '1')
    pack12 = Parcel('12',
                    '3575 W Valley Central Station bus Loop',
                    '22 00',
                    'Salt Lake City',
                    '84119',
                    '1')
    pack13 = Parcel('13',
                    '2010 W 500 S',
                    '10 30',
                    'Salt Lake City',
                    '84104',
                    '2')
    pack13.set_required_truck(1)
    pack14 = Parcel('14',
                    '4300 S 1300 E',
                    '10 30',
                    'Millcreek',
                    '84117',
                    '88')
    pack14.set_required_truck(1)
    pack14.set_priority(1)
    pack15 = Parcel('15',
                    '4580 S 2300 E',
                    '09 00',
                    'Holladay',
                    '84117',
                    '4')
    pack15.set_required_truck(1)
    pack15.set_priority(1)
    pack16 = Parcel('16',
                    '4580 S 2300 E',
                    '10 30',
                    '4580 S 2300 E',
                    '84117',
                    '88')
    pack16.set_required_truck(1)
    pack16.set_priority(1)
    pack17 = Parcel('17',
                    '3148 S 1100 W',
                    '22 00',
                    'Salt Lake City',
                    '84119',
                    '2')
    pack18 = Parcel('18',
                    '1488 4800 S',
                    '22 00',
                    'Salt Lake City',
                    '84123',
                    '6')
    pack18.set_required_truck(2)
    pack19 = Parcel('19',
                    '177 W Price Ave',
                    '22 00',
                    'Salt Lake City',
                    '84115',
                    '37')
    pack19.set_required_truck(1)
    pack20 = Parcel('20',
                    '3595 Main St',
                    '10 30',
                    'Salt Lake City',
                    '84115',
                    '37')
    pack20.set_required_truck(1)
    pack20.set_priority(1)
    pack21 = Parcel('21',
                    '3595 Main St',
                    '22 00',
                    'Salt Lake City',
                    '84115',
                    '3')
    pack22 = Parcel('22',
                    '6351 South 900 East',
                    '22 00',
                    'Murray',
                    '84121',
                    '2')
    pack23 = Parcel('23',
                    '5100 South 2700 West',
                    '22 00',
                    'Salt Lake City',
                    '84118',
                    '5')
    pack24 = Parcel('24',
                    '5025 State St',
                    '22 00',
                    'Murray',
                    '84107',
                    '7')
    pack25 = Parcel('25',
                    '5383 South 900 East #104',
                    '10 30',
                    'Salt Lake City',
                    '84117',
                    '7',
                    'delayed until 0905')
    pack25.set_priority(0)
    pack26 = Parcel('26',
                    '5383 South 900 East #104',
                    '22 00',
                    'Salt Lake City',
                    '84117',
                    '25')
    pack27 = Parcel('27',
                    '1060 Dalton Ave S',
                    '22 00',
                    'Salt Lake City',
                    '84104',
                    '5')
    pack28 = Parcel('28',
                    '2835 Main St',
                    '22 00',
                    'Salt Lake City',
                    '84115',
                    '7',
                    'delayed until 0905')
    pack29 = Parcel('29',
                    '1330 2100 S',
                    '10 30',
                    'Salt Lake City',
                    '84106',
                    '2')
    pack29.set_priority(1)
    pack30 = Parcel('30',
                    '300 State St',
                    '10 30',
                    'Salt Lake City',
                    '84103',
                    '1')
    pack30.set_priority(1)
    pack31 = Parcel('31',
                    '3365 S 900 W',
                    '10 30',
                    'Salt Lake City',
                    '84119',
                    '1')
    pack31.set_priority(1)
    pack32 = Parcel('32',
                    '3365 S 900 W',
                    '22 00',
                    'Salt Lake City',
                    '84119',
                    '1',
                    'delayed until 0905')
    pack33 = Parcel('33',
                    '2530 S 500 E',
                    '22 00',
                    'Salt Lake City',
                    '84106',
                    '1')
    pack34 = Parcel('34',
                    '4580 S 2300 E',
                    '10 30',
                    'Holladay',
                    'zip2',
                    '2')
    pack34.set_priority(1)
    pack35 = Parcel('35',
                    '1060 Dalton Ave S',
                    '22 00',
                    'Salt Lake City',
                    '84104',
                    '88')
    pack36 = Parcel('36',
                    '2300 Parkway Blvd',
                    '22 00',
                    'West Valley City',
                    '84119',
                    '88')
    pack36.set_required_truck(2)
    pack37 = Parcel('37',
                    '410 S State St',
                    '10 30',
                    'Salt Lake City',
                    '84111',
                    '2')
    pack37.set_priority(1)
    pack38 = Parcel('38',
                    '410 S State St',
                    '22 00',
                    'Salt Lake City',
                    '84111',
                    '9')
    pack38.set_required_truck(2)
    pack39 = Parcel('39',
                    '2010 W 500 S',
                    '22 00',
                    'Salt Lake City',
                    '84104',
                    '9')
    pack40 = Parcel('40',
                    '380 W 2880 S',
                    '10 30',
                    'Salt Lake City',
                    '84115',
                    '45')
    pack40.set_priority(1)
    hashmap.insert(pack01)
    hashmap.insert(pack02)
    hashmap.insert(pack03)
    hashmap.insert(pack04)
    hashmap.insert(pack05)
    hashmap.insert(pack06)
    hashmap.insert(pack07)
    hashmap.insert(pack08)
    hashmap.insert(pack09)
    hashmap.insert(pack10)
    hashmap.insert(pack11)
    hashmap.insert(pack12)
    hashmap.insert(pack13)
    hashmap.insert(pack14)
    hashmap.insert(pack15)
    hashmap.insert(pack16)
    hashmap.insert(pack17)
    hashmap.insert(pack18)
    hashmap.insert(pack19)
    hashmap.insert(pack20)
    hashmap.insert(pack21)
    hashmap.insert(pack22)
    hashmap.insert(pack23)
    hashmap.insert(pack24)
    hashmap.insert(pack25)
    hashmap.insert(pack26)
    hashmap.insert(pack27)
    hashmap.insert(pack28)
    hashmap.insert(pack29)
    hashmap.insert(pack30)
    hashmap.insert(pack31)
    hashmap.insert(pack32)
    hashmap.insert(pack33)
    hashmap.insert(pack34)
    hashmap.insert(pack35)
    hashmap.insert(pack36)
    hashmap.insert(pack37)
    hashmap.insert(pack38)
    hashmap.insert(pack39)
    hashmap.insert(pack40)
    print(hashmap)


# all verified
distances = [
    [
        'HUB',
        0.0
    ],
    [
        '1060 Dalton Ave S',
        7.2, 0.0
    ],
    [
        '1330 2100 S',
        3.8, 7.1, 0.0
    ],
    [
        '1488 4800 S',
        11.0, 6.4, 9.2,
        0.0
    ],
    [
        '177 W Price Ave',
        2.2, 6.0, 4.4,
        5.6, 0.0
    ],
    [
        '195 W Oakland Ave',
        3.5, 4.8, 2.8,
        6.9, 1.9, 0.0
    ],
    [
        '2010 W 500 S',
        10.9, 1.6, 8.6,
        8.6, 7.9, 6.3,
        0.0
    ],
    [
        '2300 Parkway Blvd',
        8.6, 2.8, 6.3,
        4.0, 5.1, 4.3,
        4.0, 0.0
    ],
    [
        '233 Canyon Rd',
        7.6, 4.8, 5.3,
        11.1, 7.5, 4.5,
        4.2, 7.7, 0.0
    ],
    [
        '2530 S 500 E',
        2.8, 6.3, 1.6,
        7.3, 2.6, 1.5,
        8.0, 9.3, 4.8,
        0.0
    ],
    [
        '2600 Taylorsville Blvd',
        6.4, 7.3, 10.4,
        1.0, 6.5, 8.7,
        8.6, 4.6, 11.9,
        9.4, 0.0
    ],
    # good below
    [
        '2835 Main St',
        3.2, 5.2, 3.0,
        6.4, 1.5, 0.8,
        6.9, 4.8, 4.7,
        1.1, 7.3, 0.0
    ],
    [
        '300 State St',
        7.6, 4.8, 5.3,
        11.1, 7.5, 4.5,
        4.2, 7.7, 0.6,
        5.1, 12, 4.7,
        0.0
    ],
    [
        '3060 Lester St',
        5.2, 3.0, 6.5,
        3.9, 3.2, 3.9,
        4.2, 1.6, 7.6,
        4.6, 4.9, 3.5,
        7.3, 0.0
    ],
    [
        '3148 S 1100 W',
        4.4, 4.6, 5.6,
        4.3, 2.4, 3.0,
        8.0, 3.3, 7.8,
        3.7, 5.2, 2.6,
        7.8, 1.3, 0.0
    ],
    # good below
    [
        '3365 S 900 W',
        3.7, 4.5, 5.8,
        4.4, 2.7, 3.8,
        5.8, 3.4, 6.6,
        4.0, 5.4, 2.9,
        6.6, 1.5, 0.6,
        0.0
    ],
    [
        '3575 W Valley Central Station bus Loop',
        7.6, 7.4, 5.7,
        7.2, 1.4, 5.7,
        7.2, 3.1, 7.2,
        6.7, 8.1, 6.3,
        7.2, 4.0, 6.4,
        5.6, 0.0
    ],
    [
        '3595 Main St',
        2.0, 6.0, 4.1,
        5.3, 0.5, 1.9,
        7.7, 5.1, 5.9,
        2.3, 6.2, 1.2,
        5.9, 3.2, 2.4,
        1.6, 7.1, 0.0
    ],
    [
        '380 W 2880 S',
        3.6, 5.0, 3.6,
        6.0, 1.7, 1.1,
        6.6, 4.6, 5.4,
        1.8, 6.9, 1.0,
        5.4, 3.0, 2.2,
        1.7, 6.1, 1.6,
        0.0
    ],
    [
        '410 S State St',
        6.5, 4.8, 4.3,
        10.6, 6.5, 3.5,
        3.2, 6.7, 1.0,
        4.1, 11.5, 3.7,
        1.0, 6.9, 6.8,
        6.4, 7.2, 4.9,
        4.4, 0.0
    ],
    #verified below this line
    [
        '4300 S 1300 E',
        1.9, 9.5, 3.3,
        5.9, 3.2, 4.9,
        11.2,8.1, 8.5,
        3.8, 6.9, 4.1,
        8.5, 6.2, 5.3,
        4.9, 10.6, 3.0,
        4.6, 7.5, 0.0
    ],
    [
        '4580 S 2300 E',
        3.4, 10.9, 5.0,
        7.4, 5.2, 6.9,
        12.7, 10.4, 10.3,
        5.8, 8.3, 6.2,
        10.3, 8.2, 7.4,
        6.9, 12.0, 5.0,
        6.6, 9.3, 2.0,
        0.0
    ],
    [
        '5025 State St',
        2.4, 8.3, 6.1,
        4.7, 2.5, 4.2,
        10.0, 7.8, 7.8,
        4.3, 4.1, 3.4,
        7.8, 5.5, 4.6,
        4.2, 9.4, 2.3,
        3.9, 6.8, 2.9,
        4.4, 0.0
    ],
    # everything below this verified
    [
        '5100 South 2700 West',
        6.4, 6.9, 9.7,
        0.6, 6.0, 9.0,
        8.2, 4.2, 11.5,
        7.8, 0.4, 6.9,
        11.5,4.4, 4.8,
        5.6, 7.5, 5.5,
        6.5, 11.4, 6.4,
        7.9, 4.5, 0.0
    ],
    [
        '5383 South 900 East #104',
        2.4, 10, 6.1,
        6.4, 4.2, 5.9,
        11.7, 9.5, 9.5,
        4.8, 4.9, 5.2,
        9.5, 7.2, 6.3,
        5.9, 11.1, 4.0,
        5.6, 8.5, 2.8,
        3.4, 1.7, 5.4,
        0.0
    ],
    [
        '600 E 900 South',
        5.0, 4.4, 2.8,
        10.1, 5.4, 3.5,
        5.1, 6.2, 2.8,
        3.2, 11.0, 3.7,
        2.8, 6.4, 6.5,
        5.7, 6.2, 5.1,
        4.3, 1.8, 6.0,
        7.9, 6.8, 10.6,
        7.0, 0.0
    ],
    [
        '6351 South 900 East',
        3.6, 13.0, 7.4,
        10.1, 5.5, 7.2,
        14.2, 10.7, 14.1,
        6.0, 6.8, 6.4,
        14.1, 10.5, 8.8,
        8.4, 13.6, 5.2,
        6.9, 13.1, 4.1,
        4.7, 3.1, 7.8,
        1.3, 8.3, 0.0
    ]
]

# O(n)
def get_address_index(address: str):
    """Takes an address string and returns the index value of that string.
    Will be an internal helper function, no need to import to other modules
    at least once testing if finished.  fixme delete excess comment"""
    #print("in get_address_index: {}".format(address))
    for i in range(len(distances)):
        #print(distances[i][0])
        if distances[i][0] == address:
            print("index is: {}".format(i))
            return i

# O(1)
def get_distance_between_addresses(current_location: str, next_location: str):
    # Takes two address strings and returns the distance between those addresses
    #print('\n**** Starting get distance function')
    #print("address 1: {}  address 2: {}".format(current_location, next_location))
    row = get_address_index(current_location)
    col = get_address_index(next_location)
    #print("indexes are: {} and {}".format(row, col))
    # Because of the way the distance data spreadsheet (and my own 2d array)
    # are filled out, it is necessary for the first index to be >= the second index.
    # This 'if' statement fixes that.
    if row < col:
        #print("The current index has a value lower than the next index, reversing.")
        temp = row
        row = col
        col = temp
    #print("indexes are: {} and {}".format(row, col))
    #print('***** finishing get distance function\n')
    # Need to offset column number by one to skip address string. Adding 1 to column fixes this
    return distances[row][col + 1]

