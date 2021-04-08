from datetime import datetime

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
        #self.__d_deadline = datetime.strptime(__d_deadline, '%m %d %Y %H %M %S') #convert input string to datetime
        self.__d_deadline = datetime.strptime(d_deadline, '%H %M') #convert input string to datetime
        self.__d_address = d_address
        self.__id = id
        self.__note = ''
        self.__required_truck = -1 # If negative number, any truck will do. Not sure if this will be used.
        self.__siblings = []       # This might be useful if parcel should go on a certain truck. May not be used.

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

    def setStatusEnRoute(self):
        self.__status = 'en route'

    def setStatusDelivered(self):
        self.__status = 'delivered'

    def setStatusNotReady(self):
        self.__status = 'not ready'

    def setNote(self, note: str):
        self.__note = note

    def set_siblings(self, siblings):
        self.__siblings = siblings

    def set_required_truck(self, truck: int):
        self.__required_truck = truck

    def get_id(self):
        return self.__id


