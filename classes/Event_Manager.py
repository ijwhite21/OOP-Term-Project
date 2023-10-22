from classes.Event_Attendee import Event_Attendee
from classes.Event import Event
from classes.Attendee import Attendee

# This class is meant to manage the Events, Attendees, and Event_Attendees
class EventManager(object):
    def __init__(self):
        self.__events = []
        self.__attendees = []
        self.__event_attendees = []
        self.__attendeeUID = 0
        self.__eventUID = 0

    @property
    def events(self):
        return self.__events

    @property
    def attendees(self):
        return self.__attendees

    @property
    def event_attendees(self) -> list:
        return self.__event_attendees

    @property
    def attendeeUID(self):
        return self.__attendeeUID

    @property
    def eventUID(self):
        return self.__eventUID

    @events.setter
    def events(self, e: list):
        self.__events = e

    @attendees.setter
    def attendees(self, a: list):
        self.__attendees = a

    @event_attendees.setter
    def event_attendees(self, ea: list):
        self.__event_attendees = ea

    @attendeeUID.setter
    def attendeeUID(self, a):
        self.__attendeeUID = a

    @eventUID.setter
    def eventUID(self, e):
        self.__eventUID = e

    # This function appends a new event object onto the 'events' array
    def add_event(self, e: dict):
        x = e
        self.eventUID = max(self.eventUID, e["UID"]) + 1
        self.events.append(Event(e))
        self.sort_events()

    # This function appends a new attendee object onto the array 'attendees'
    def add_attendee(self, a: dict):
        self.attendeeUID = max(self.attendeeUID, a["UID"]) + 1
        self.__attendees.append(Attendee(a))
        self.sort_attendees()

    # This will append a new Event_Attendee object into the array 'event_attendees'
    def add_event_attendee(self, event: Event, attendee: Attendee):
        already = False
        # Check if the event attendee already exists
        for x in self.event_attendees:
            if x.event == event and x.attendee == attendee:
                already = True
                break
        # if the event_attendee doesn't already exist, create it
        if already == False:
            self.__event_attendees.append(Event_Attendee(event, attendee))

    def sort_attendees(self):
        # sort the list by lastname (alphabetically)
        self.attendees.sort(key=lambda x: x.lastname)
    #This function will sort the events by date and time
    def sort_events(self):
        self.events.sort(key=lambda x: x.date, reverse=False)

    def __str__(self):
        return "\n".join(map(str, self.event_attendees))
        # return "\n".join(map(str, self.attendees))
        # return "\n".join(map(str, self.events))