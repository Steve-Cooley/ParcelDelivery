from datetime import datetime


# This is my Parcel (package) class.  I wanted to avoid the word "package" because it has another meaning in
# Python. The methods are all simple setter and getter type, all O(n)
class Parcel:
    # time: O(1) space: O(1)
    # This constructor initializes all of the object's fields.  Some of the fields won't be used at time of
    # submission due to time constraints.
    def __init__(self, id: str, d_address: str, d_deadline: str, d_city: str, d_zip: str, weight: str,
                 status: str = 'waiting'):
        self.__status = status
        self.__weight = weight
        self.__d_zip = d_zip
        self.__d_city = d_city
        self.__d_deadline = datetime.strptime(d_deadline, "%H %M")  # convert input string to datetime
        self.__d_address = d_address
        self.__id = id
        self.__note = ''
        # Specifies truck. Negative number means any truck.
        self.__required_truck = -1
        # List of siblings (packages go together). May help loading trucks. Not used at time of submission
        self.__siblings = []
        # (0-3), Intended to help with loading and ensuring timely delivery. 0 is highest.
        self.__delivery_priority = 2
        # (0-1) may help with chained loaded_parcels.  0 lowest priority. 0-1
        self.__load_priority = 1  # (0-1) may help with chained loaded_parcels.  0 lowest priority. 0-1
        self.__ready_time = datetime.strptime("08 00", "%H %M")

    # time: O(1) space: O(1)
    # This override helps report the status of all parcels..
    def __str__(self):
        rstring = '|' + self.__id + '|' + \
                  self.__d_address + '|' + \
                  self.__d_deadline.strftime('%H:%M') + '|' + \
                  self.__d_city + '|' + \
                  self.__d_zip + '|' + \
                  self.__weight + '|status: ' + \
                  self.__status + '|'
        return rstring

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_ready_time(self, ready_time: datetime):
        self.__ready_time = ready_time

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_status_on_truck(self, truck_number: int):
        self.__status = 'truck{}'.format(truck_number)

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_status_delivered(self, ts: datetime):
        self.__status = 'delivered at {}'.format(ts.strftime('%H:%M'))

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_status_late(self, ts: datetime):
        self.__status = '@@@@@@@@@@ PACKAGE LATE: {}'.format(ts.strftime('%H:%M'))

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_status_waiting(self):
        self.__status = 'waiting'

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def get_status(self):
        return self.__status

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_note(self, note: str):
        self.__note = note

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_siblings(self, siblings):
        self.__siblings = siblings

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_required_truck(self, truck: int):
        self.__required_truck = truck

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def get_required_truck(self):
        return self.__required_truck

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def get_id(self):
        return self.__id

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def get_d_address(self):
        return self.__d_address

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_d_address(self, address: str):
        self.__d_address = address

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_priority(self, priority: int):
        self.__delivery_priority = priority

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def get_priority(self):
        return self.__delivery_priority

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def set_deadline(self, deadline: datetime):
        self.__d_deadline = deadline

    # time: O(1) space: O(1)
    # One of a number of very simple methods that get and set attributes in parcel objects.
    def get_deadline(self):
        return self.__d_deadline
