from classes.Attendee import Attendee
from classes.Event import Event

# This class represents a tuple of Event and Attendee objects. Meaning the Attendee is attending the Event
class Event_Attendee(object):
    def __init__(self, e: Event, a: Attendee):
        self.__event: Event = e
        self.__attendee: Attendee = a
        self.__attendee_name = f"{a.firstname} {a.lastname}"
        self.state = ""

    @property
    def event(self):
        return self.__event

    @property
    def attendee(self):
        return self.__attendee

    @property
    def attendee_name(self):
        return self.__attendee_name

    def __str__(self):
        return "{} {} going to {}".format(self.attendee.firstname, self.attendee.lastname, self.event.name)