from datetime import datetime, timedelta


# This is my Parcel (package) class.  I wanted to avoid the word "package" because it has another meaning in
# Python.
class Parcel:
    # This constructor just initializes all of the object's fields.
    def __init__(self, id: str, d_address: str, d_deadline: str, d_city: str, d_zip: str, weight: str,
                 status: str = 'waiting'):
        self.__status = status
        self.__weight = weight
        self.__d_zip = d_zip
        self.__d_city = d_city
        # self.__d_deadline = datetime.strptime(__d_deadline, '%m %d %Y %H %M %S') #convert input string to datetime
        self.__d_deadline = datetime.strptime(d_deadline, "%H %M")  # convert input string to datetime
        self.__d_address = d_address
        self.__id = id
        self.__note = ''
        # Specifies truck. Negative number means any truck.
        self.__required_truck = -1
        # List of siblings (packages go together). May help loading trucks.
        self.__siblings = []
        # (0-3), may not be used, but is intended to help with loading and ensuring timely delivery. 0 is highest.
        self.__delivery_priority = 2
        # (0-1) may help with chained loaded_parcels.  0 lowest priority. 0-1
        self.__load_priority = 1  # (0-1) may help with chained loaded_parcels.  0 lowest priority. 0-1
        self.__ready_time = datetime.strptime("08 00", "%H %M")

    # This override function returns a string containing all components in the object.  My intention is so use this for
    # requirement F.  Early days though, not sure if this will work.
    def __str__(self):
        rstring = '|' + self.__id + '|' + \
                  self.__d_address + '|' + \
                  self.__d_deadline.strftime('%H:%M') + '|' + \
                  self.__d_city + '|' + \
                  self.__d_zip + '|' + \
                  self.__weight + '|' + \
                  self.__status + '|'
        return rstring

    def set_ready_time(self, ready_time: datetime):
        self.__ready_time = ready_time

    def set_status_on_truck(self, truck_number: int):
        self.__status = 'truck{}'.format(truck_number)

    def set_status_delivered(self, ts: datetime):
        self.__status = 'delivered at {}'.format(ts.strftime('%H:%M'))
        # needs timestamp todo

    def set_status_late(self, ts: datetime):
        self.__status = '@@@@@@@@@@ PACKAGE LATE: {}'.format(ts.strftime('%H:%M'))

    # fixme, I don't think this is ever used
    def set_status_not_ready(self):
        self.__status = 'not ready'

    def set_status_waiting(self):
        self.__status = 'waiting'

    def get_status(self):
        return self.__status

    def set_note(self, note: str):
        self.__note = note

    def set_siblings(self, siblings):
        self.__siblings = siblings

    def set_required_truck(self, truck: int):
        self.__required_truck = truck

    def get_required_truck(self):
        return self.__required_truck

    def get_id(self):
        return self.__id

    def get_d_address(self):
        return self.__d_address

    def set_priority(self, priority: int):
        self.__delivery_priority = priority

    def get_priority(self):
        return self.__delivery_priority

    def set_deadline(self, deadline: datetime):
        self.__d_deadline = deadline

    def get_deadline(self):
        return self.__d_deadline
