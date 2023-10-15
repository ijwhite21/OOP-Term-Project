from classes.Attendee import Attendee
from classes.Event import Event
from classes.Event_Attendee import Event_Attendee
from classes.Event_Manager import EventManager
from UI.GUI import Gui

# This imports the attendees.json and events.json which will most likely not be used for the project anymore
import json
import calendar
with open('attendees.json') as f:
    attendee_data = json.load(f)
with open('events.json') as g:
    event_data = json.load(g)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #initialize the EventManager object (there's only 1 instance of it)
    em = EventManager()
    # initialize the gui object (from tkinter)
    gui = Gui(em)

    # # add all events from the events.json into the event manager
    # for x in event_data["university_events"]:
    #     em.add_event(x)
    #
    # # add all attendees from the attendees.json into the event manager
    # for x in attendee_data:
    #     em.add_attendee(x)
    #
    # # create a few event_attendees ie pairing up some attendees with some events for testing
    # for i in range(len(event_data["university_events"])):
    #     em.add_event_attendee(em.events[i], em.attendees[i])
    #
    # # demonstrate the event managers print function
    # print("-Event_Attendees-")
    # print(em)
    #
    # # demonstrate the attendee print function
    # print("\n-Attendees-")
    # for x in em.attendees:
    #     print(x)
    #
    # # demonstrate the event print function
    # print("\n-Events-")
    # for x in em.events:
    #     print(x)



    # yy = 2023
    # mm = 9
    # print(calendar.month(yy, mm))
    # print(calendar.monthcalendar(yy, mm))

    # attendee1 = Attendee(attendee_data[0])
    # event1 = Event(event_data["university_events"][0])
    # event_attendee1 = Event_Attendee(event1, attendee1)
    # print(event1)
    # print("")
    # print(attendee1)
    # print(event_attendee1)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
