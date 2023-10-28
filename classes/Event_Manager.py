from classes.Event_Attendee import Event_Attendee
from classes.Event import Event
from classes.Contact import Contact

# This class is meant to manage the Events, Contacts, and Event_Attendees
# This class also directly communicates with the GUI as the GUI "has" an EventManager object (aggregation)

# This class has a list of Event objects, a list of Contact objects, and a list of Event_Attendee objects

class EventManager(object):
    # constructor
    def __init__(self):
        self.__events: list[Event] = []
        self.__contacts: list[Contact] = []
        self.__event_attendees: list[Event_Attendee] = []
        self.__contactUID: int = 0
        self.__eventUID: int = 0

    # getters
    @property
    def events(self):
        return self.__events

    @property
    def contacts(self):
        return self.__contacts

    @property
    def event_attendees(self) -> list:
        return self.__event_attendees

    @property
    def contactUID(self):
        return self.__contactUID

    @property
    def eventUID(self):
        return self.__eventUID

    # setters
    @events.setter
    def events(self, e: list[Event]):
        self.__events = e

    @contacts.setter
    def contacts(self, a: list[Contact]):
        self.__contacts = a

    @event_attendees.setter
    def event_attendees(self, ea: list[Event_Attendee]):
        self.__event_attendees = ea

    @contactUID.setter
    def contactUID(self, a):
        self.__contactUID = a

    @eventUID.setter
    def eventUID(self, e):
        self.__eventUID = e

    # This function appends a new event object onto the 'events' array
    # This is called by the GUI and a dictionary is passed
    # other than loading in the json data on startup, the dictionary passed as an argument is made in the GUI class in the form_submission_event() function
    def add_event(self, e: dict):
        # this makes sure the new UID for the event is not equal to any other (increments by 1)
        self.eventUID = max(self.eventUID, e["UID"]) + 1
        # pass the same argument into the Event constructor to add an Event object to the events list
        self.events.append(Event(e))
        # sort events by date
        self.sort_events()

    # This function appends a new contact object onto the array 'contacts'
    # other than loading in the json data on startup, the dictionary passed as an argument is made in the GUI class in the form_submission_contact() function
    def add_contact(self, c: dict):
        # this makes sure the new UID for the contact is not equal to any other (increments by 1)
        self.contactUID = max(self.contactUID, c["UID"]) + 1
        # append a contact onto the contacts list passing the dictionary "c" as an argument
        self.__contacts.append(Contact(c))
        # sort contacts by lastname
        self.sort_contacts()

    # This will append a new Event_Attendee object into the array 'event_attendees'
    # an event and a contact are passed in as arguments and then passed again into Event_Attendee's constructor
    def add_event_attendee(self, event: Event, contact: Contact):
        # This bool will set to True if the event_attendee that's being added is already in the list
        already: bool = False
        # Check if the event attendee already exists
        for x in self.event_attendees:
            if x.event == event and x.contact == contact:
                already = True
                break
        # if the event_attendee doesn't already exist, create it
        if already == False:
            # pass the same arguments into the Event_Attendee constructor
            self.__event_attendees.append(Event_Attendee(event, contact))

    # This sorts the contacts in the list by lastname
    def sort_contacts(self):
        # sort the list by lastname (alphabetically)
        self.contacts.sort(key=lambda x: x.lastname)

    #This function will sort the events by date
    def sort_events(self):
        self.events.sort(key=lambda x: x.date, reverse=False)

    # This function defines what happens when you print the object as text ie print(Event_Manager)
    def __str__(self):
        # This will print all of the event_attendee objects in self.event_attendees separated by a new line
        return "\n".join(map(str, self.event_attendees))