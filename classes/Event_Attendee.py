from classes.Contact import Contact
from classes.Event import Event

"""
This class represents a tuple of 1 Event and 1 Contact object, meaning the Contact is attending the Event.
This is its own class because there will be attributes associated to a contact attending an event ie
whether they need a parking pass, special accommodations, etc. 

For now, the "memo" attribute is a catch-all for these, but in the future, more attributes will be added
"""

class Event_Attendee(object):
    # an Event object and Contact object are passed into the constructor, essentially creating a tuple object
    def __init__(self, e: Event, c: Contact):
        self.__event: Event = e
        self.__contact: Contact = c
        # this is so the user can keep a memo for each event attendee
        self.__memo: str = ""

    # getters
    @property
    def event(self):
        return self.__event

    @property
    def contact(self):
        return self.__contact

    @property
    def memo(self):
        return self.__memo

    # setters
    @memo.setter
    def memo(self, m: str):
        self.__memo = m

    # This function defines what happens when you print the object as text ie print(Event_Attendee)
    def __str__(self):
        """
        python has a few ways of streamlining concatenation of strings.
        each time there's a {} in the string, that represents a variable.
        notice at the end of the string, ".format()"
        the variables passed into this function will replace each {} (in order)
        """
        return "{} {}\nattending\n{}".format(self.contact.firstname, self.contact.lastname, self.event.name)