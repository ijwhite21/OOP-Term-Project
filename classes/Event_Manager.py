from classes.Event_Attendee import Event_Attendee
from classes.Event import Event
from classes.Attendee import Attendee

# This class is meant to manage the Events, Attendees, and Event_Attendees
class EventManager(object):
    def __init__(self):
        self.__events = []
        self.__attendees = []
        self.__event_attendees = []

    @property
    def events(self):
        return self.__events

    @property
    def attendees(self):
        return self.__attendees

    @property
    def event_attendees(self) -> list:
        return self.__event_attendees

    @events.setter
    def events(self, e: list):
        self.__events = e

    @attendees.setter
    def attendees(self, a: list):
        self.__attendees = a

    @event_attendees.setter
    def event_attendees(self, ea: list):
        self.__event_attendees = ea

    # This function appends a new event object onto the 'events' array
    def add_event(self, e: dict):
        x = e
        self.events.append(Event(e))

    # This function appends a new attendee object onto the array 'attendees'
    def add_attendee(self, a: dict):
        self.__attendees.append(Attendee(a))

    # This will append a new Event_Attendee object into the array 'event_attendees'
    def add_event_attendee(self, event: Event, attendee: Attendee):
        self.__event_attendees.append(Event_Attendee(event, attendee))

    def __str__(self):
        # return "\n".join(map(str, self.event_attendees))
        return "\n".join(map(str, self.attendees))
        # return "\n".join(map(str, self.events))