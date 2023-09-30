from classes.Attendee import Attendee
from classes.Event import Event

class Event_Attendee(object, event, attendee):
    def __init__(self):
        self.__event = event
        self.__attendee = attendee
        self.__state = ""

        @property
        def event(self):
            return self.__event
