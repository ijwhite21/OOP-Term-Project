from classes.Attendee import Attendee
from classes.Event import Event

# This class represents a tuple of Event and Attendee objects. Meaning the Attendee is attending the Event
class Event_Attendee(object):
    def __init__(self, e: Event, a: Attendee):
        self.__event: Event = e
        self.__attendee: Attendee = a
        self.__memo: str = ""
        self.state: str = ""

    @property
    def event(self):
        return self.__event

    @property
    def attendee(self):
        return self.__attendee

    @property
    def memo(self):
        return self.__memo

    @memo.setter
    def memo(self, m):
        self.__memo = m

    def __str__(self):
        return "{} {}\nattending\n{}".format(self.attendee.firstname, self.attendee.lastname, self.event.name)