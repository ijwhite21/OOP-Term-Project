from classes.Attendee import Attendee
from classes.Event import Event
# from classes.Event_Attendee import Event_Attendee

import json
import calendar
with open('cs_directory.json') as f:
    csd = json.load(f)
with open('events.json') as g:
    event_data = json.load(g)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # # print all the users
    for i in range(len(csd)):
        person = Attendee(csd[i])
        print(person)

    # yy = 2023
    # mm = 9
    # print(calendar.month(yy, mm))
    # print(calendar.monthcalendar(yy, mm))

    #print all events
    for i in range(len(event_data["university_events"])):
        event1 = Event(event_data["university_events"][i])
        print(event1)
        print("")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
