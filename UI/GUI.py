from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from classes.Event_Manager import EventManager
from classes.Attendee import Attendee

class Gui:
    # Gui constructor. NOTE: an Event_Manager object is passed into the constructor. This is so that the Gui class can pass data into it.
    def __init__(self, eventmanager):
        #establish font
        self.fontsize = 18
        self.font = 'Arial'
        # We've instantiated an event manager in main. We then aggregate it onto the Gui so that it can receive form submissions etc
        self.em = eventmanager
        # This variable is used to create an Event_Attendee object later on
        self.current_event = 0
        # These are used to destroy the dropdown lists on the same page
        self.is_current_attendees_dropdown = False
        self.is_add_attendees_dropdown = False
        #This adds the tk functionality to the Gui class
        self.root = Tk()
        # this is where a lot of the visuals can be declared (kinda like CSS) (inbetween the dotted lines)
        # This sets the text in the window border
        self.root.title("OOP TERM PROJECT")
        # This line sets the resolution
        self.root.geometry("640x480")
        # This is part of the closing function (whenever you ex out of the program)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        #create the frame for the side buttons "Create Attendee", "Create Event", etc (this will always be here)
        self.sidebuttons = LabelFrame(self.root, padx=2, pady=10)
        self.sidebuttons.pack(side="left", expand=False, fill="both")

        #add attendee button
        self.button_add_attendee = Button(self.sidebuttons, text="Create Attendee", font=(self.font, self.fontsize), command=self.attendee_screen)
        self.button_add_attendee.pack()

        #add event button
        self.button_add_event = Button(self.sidebuttons, text="Create Event", font=(self.font, self.fontsize), command=self.event_screen)
        self.button_add_event.pack()

        #display attendees
        self.button_display_attendees = Button(self.sidebuttons, text="Display Attendees", font=(self.font, self.fontsize), command=self.display_attendees)
        self.button_display_attendees.pack()

        # display events
        self.button_display_events = Button(self.sidebuttons, text="Display Events", font=(self.font, self.fontsize), command=self.display_events)
        self.button_display_events.pack()


        #establish the frame that will house each type of form. this will be cleared, then repopulated will the selected form or "state"
        self.frame = LabelFrame(self.root, padx=0, pady=10)
        self.frame.pack(side="right", expand=True, fill="both")

        # this is the loop that refreshes the GUI
        self.root.mainloop()

    # This function is called whenever you try to close the window
    def on_closing(self):
        # if messagebox.askyesno(title="Quit?", message="Leaving?... Seriously?"):
            self.root.destroy()

    # This clears the frame of all widgets. This is called every time the menu changes to another screen
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # this function disables the button you have clicked (mainly to mark which page you are currently on)
    def button_state(self, button: str):
        self.button_add_attendee["state"] = "normal"
        self.button_add_event["state"] = "normal"
        self.button_display_attendees["state"] = "normal"
        self.button_display_events["state"] = "normal"

        if button == "add_attendee":
            self.button_add_attendee["state"] = "disabled"

        elif button == "add_event":
            self.button_add_event["state"] = "disabled"

        elif button == "display_attendees":
            self.button_display_attendees["state"] = "disabled"

        elif button == "display_events":
            self.button_display_events["state"] = "disabled"

    # This function creates the "Create Attendee" screen
    def attendee_screen(self):
        self.clear_frame()

        self.button_state("add_attendee")
        # these are label definitions followed by text entry box definitions for each attribute
        # this label will simply say 'First Name' above the text box
        self.label_firstname = Label(self.frame, text="First Name", font=(self.font, self.fontsize))
        # this text box is for entering the first name
        self.firstname_entry = Entry(self.frame)
        self.label_lastname = Label(self.frame, text="Last Name", font=(self.font, self.fontsize))
        self.lastname_entry = Entry(self.frame)
        self.label_email = Label(self.frame, text="Email", font=(self.font, self.fontsize))
        self.email_entry = Entry(self.frame)
        self.label_phone = Label(self.frame, text="Phone #", font=(self.font, self.fontsize))
        self.phone_entry = Entry(self.frame)

        # the pack() function will put the Gui component in the next available
        # space on the screen. It's a quick fix. There's better looking ways to
        # do it where you can specify padding etc.
        self.label_firstname.pack()
        self.firstname_entry.pack()
        self.label_lastname.pack()
        self.lastname_entry.pack()
        self.label_email.pack()
        self.email_entry.pack()
        self.label_phone.pack()
        self.phone_entry.pack()

        # pressing this button in the Gui will create a new attendee with the entered info from the above text boxes
        self.button = Button(self.frame, text="Create", font=(self.font, self.fontsize), command=self.form_submission_attendee)
        self.button.pack()

    # This function is called whenever you click the "Create" button on the "Create Attendee" screen
    def form_submission_attendee(self):
        # a dictionary is created with attendee info then used to create an attendee
        a = {
            "FirstName": self.firstname_entry.get(),
            "LastName": self.lastname_entry.get(),
            "UID": self.em.attendeeUID,
            "EmailAddress": self.email_entry.get(),
            "Dept": "Computer Science",
            "Title": "Assistant Professor",
            "Phone": self.phone_entry.get(),
            "Building": "Bruner Hall (BRUN) 232",
            "POBox": "5101"
            }

        # testing to see if the info can construct an attendee object
        # attendee1 = Attendee(a)
        # print(attendee1)
        self.em.add_attendee(a)
        # This prints the attendee onto the gui
        self.label_attendee = Label(self.frame, text="Attendee Added", font=('Arial', 18))
        self.label_attendee.pack()
        # print(self.em)

    # This function creates the "Create Event" screen
    def event_screen(self):
        self.clear_frame()

        self.button_state("add_event")
        # these are label definitions followed by text entry box definitions for each attribute
        # this label will simply say 'First Name' above the text box
        self.label_eventname = Label(self.frame, text="Event Name", font=(self.font, self.fontsize))
        # this text box is for entering the first name
        self.eventname_entry = Entry(self.frame)

        self.label_eventdate = Label(self.frame, text="Date (yyyy-mm-dd)", font=(self.font, self.fontsize))
        self.eventdate_entry = Entry(self.frame)

        self.label_eventstarttime = Label(self.frame, text="Start Time", font=(self.font, self.fontsize))
        self.eventstarttime_entry = Entry(self.frame)

        self.label_eventlocation = Label(self.frame, text="Location", font=(self.font, self.fontsize))
        self.eventlocation_entry = Entry(self.frame)

        self.label_eventduration = Label(self.frame, text="Duration (hours)", font=(self.font, self.fontsize))
        self.eventduration_entry = Entry(self.frame)

        # the pack() function will put the Gui component in the next available
        # space on the screen. It's a quick fix. There's better looking ways to
        # do it where you can specify padding etc.
        self.label_eventname.pack()
        self.eventname_entry.pack()

        self.label_eventdate.pack()
        self.eventdate_entry.pack()
        self.label_eventstarttime.pack()
        self.eventstarttime_entry.pack()
        self.label_eventlocation.pack()
        self.eventlocation_entry.pack()
        self.label_eventduration.pack()
        self.eventduration_entry.pack()

        # pressing this button in the Gui will create a new attendee with the entered info from the above text boxes
        self.button = Button(self.frame, text="Create", font=(self.font, self.fontsize), command=self.form_submission_event)
        self.button.pack()

    # This function is called when you click the "Create" button on the "Create Event" screen
    def form_submission_event(self):
        # a dictionary is created with attendee info then used to create an attendee
        a = {
            "Name": self.eventname_entry.get(),
            "Date": self.eventdate_entry.get(),
            "UID" : self.em.eventUID,
            "StartTime": self.eventstarttime_entry.get(),
            "Location": self.eventlocation_entry.get(),
            "Duration": self.eventduration_entry.get()
        }

        # testing to see if the info can construct an attendee object
        # attendee1 = Attendee(a)
        # print(attendee1)
        self.em.add_event(a)
        # This prints the attendee onto the gui
        self.label_event = Label(self.frame, text="Event Added", font=('Arial', 18))
        self.label_event.pack()

    # display all the attendees in a list
    def display_attendees(self):
        self.clear_frame()
        self.button_state("display_attendees")
        alist = []
        # get attendees in the form of a list of first and last names
        for x in self.em.attendees:
            alist.append(f"{x.lastname}, {x.firstname}")
        list_items = Variable(value=alist)
        self.listbox = Listbox(self.frame, height=len(alist), font=(self.font, self.fontsize), listvariable=list_items)
        self.listbox.bind('<<ListboxSelect>>', self.select_attendee)
        self.listbox.pack()

        # for x in self.em.attendees:
        #     self.attendee_name = Label(self.frame, text=x.firstname+" "+x.lastname, font=(self.font, self.fontsize))
        #     self.attendee_name.pack()

    # when an attendee is selected from the list to see their info
    def select_attendee(self, event):
        # get all selected indices
        selected_indices = self.listbox.curselection()
        # get selected items
        selected_events = ",".join([self.listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_events}'
        # self.label8 = Label(self.frame, text=selected_indices, font=(self.font, self.fontsize))
        # self.label8.pack()
        self.display_attendee_single(int(selected_indices[0]))

    #This will display a single attendee's info once clicked from the dropdown menu
    def display_attendee_single(self, selected_indices):
        self.clear_frame()
        self.button_back = Button(self.frame, text="Back", font=(self.font, self.fontsize), command=self.display_attendees)
        self.button_back.pack()
        e = self.em.attendees[selected_indices]
        self.label_eventsingle = Label(self.frame, text=e, font=(self.font, self.fontsize))
        self.label_eventsingle.pack()

    # display all the events in a list
    def display_events(self):
        self.clear_frame()
        self.button_state("display_events")
        elist = []
        # get attendees in the form of a list of first and last names
        for x in self.em.events:
            elist.append(f"{x.date}: {x.name}")
        list_items = Variable(value=elist)
        self.listbox_events = Listbox(self.frame, width=50, height=len(elist), font=(self.font, self.fontsize), listvariable=list_items)
        self.listbox_events.bind('<<ListboxSelect>>', self.items_selected_event)
        self.listbox_events.pack()

    # This is called whenever you select an event from the selection list
    def items_selected_event(self, event):
        # get all selected indices
        selected_indices = self.listbox_events.curselection()
        # get selected items
        selected_events = ",".join([self.listbox_events.get(i) for i in selected_indices])
        msg = f'You selected: {selected_events}'
        # self.label8 = Label(self.frame, text=selected_indices, font=(self.font, self.fontsize))
        # self.label8.pack()
        self.display_event_single(int(selected_indices[0]))

    # This displays a single event using the event's print function
    def display_event_single(self,selected_indices):
        self.clear_frame()
        self.button_back = Button(self.frame, text="Back", font=(self.font, self.fontsize),command=self.display_events)
        self.button_back.pack()
        self.current_event = selected_indices
        e = self.em.events[selected_indices]
        #get list of names of attendees not currently going to event
        # alist = []
        # for x in self.em.attendees:
        #     alist.append(x.firstname + " " + x.lastname)

        self.label_eventsingle = Label(self.frame, text=e, font=(self.font, self.fontsize))
        self.label_eventsingle.pack()

        # variable = StringVar(self.frame)
        # variable.set("")  # default value
        # w = OptionMenu(self.frame, variable, *alist)
        # w.pack()
        # This button will show current attendees for a given event
        self.button_list_attendees_going = Button(self.frame, text="Current Attendees", font=(self.font, self.fontsize), command=self.list_attendees_going)
        self.button_list_attendees_going.pack()
        # add attendee button
        self.button_list_attendees = Button(self.frame, text="Add Attendee", font=(self.font, self.fontsize), command=self.list_attendees)
        self.button_list_attendees.pack()

    # this lists the attendees going to a particular events
    def list_attendees_going(self):
        alist = []
        # check who all is going to the event ie event_attendees in the list
        for x in self.em.event_attendees:
            if x.event == self.em.events[self.current_event]:
                # alist.append(x.attendee_name)
                alist.append(f"{x.attendee.lastname}, {x.attendee.firstname}")
        list_items = Variable(value=alist)

        self.listbox_attendees_going = Listbox(self.frame, width=30, height=len(alist), listvariable=list_items)
        self.listbox_attendees_going.pack()
        self.listbox_attendees_going.bind('<<ListboxSelect>>', self.display_event_attendee_single)
        # set the state of the buttons
        self.button_list_attendees_going["state"] = "disabled"
        self.button_list_attendees["state"] = "normal"

        self.is_current_attendees_dropdown = True
        # This will delete the add_attendees dropdown list that would otherwise be in the way
        if self.is_add_attendees_dropdown:
            self.listbox_attendees.destroy()
            self.is_add_attendees_dropdown = False

    # display a single event_attendee object
    def display_event_attendee_single(self, selected_indices):
        selected_indices = self.listbox_attendees_going.curselection()
        # get selected items
        selected_event_attendee = ",".join([self.listbox_attendees_going.get(i) for i in selected_indices])
        self.clear_frame()
        self.button_back = Button(self.frame, text="Back", font=(self.font, self.fontsize),command=self.display_events)
        self.button_back.pack()

        # this will extract the first and lastnames from the selected index in the dropdownlist of attendees
        lname = selected_event_attendee.split(", ")[0]
        fname = selected_event_attendee.split(", ")[1]
        e = self.em.events[self.current_event]

        # find the event_attendee object correlating with current event and current attendee selected
        for x in self.em.event_attendees:
            if x.event == e and x.attendee.lastname == lname and x.attendee.firstname == fname:
                ea = x

        # ea = self.em.event_attendees[0]
        self.label_event_attendee = Label(self.frame, text=ea, font=(self.font, self.fontsize))
        self.label_event_attendee.pack()
        # memo textbox
        self.label_memo = Label(self.frame, text="\nMemo:", font=(self.font, self.fontsize))
        self.label_memo.pack()
        self.memotext = Text(self.frame, height=5, font=(self.font, self.fontsize))
        self.memotext.pack()
        # insert event_attendee's memo into the textbox
        self.memotext.insert(END, ea.memo)
        self.button_memo = Button(self.frame, text="Save Memo", font=(self.font, self.fontsize), command=lambda: self.set_memo(ea))
        self.button_memo.pack()

    # set the memo for an event_attendee object
    def set_memo(self, ea):
        ea.memo = self.memotext.get("1.0",'end-1c')

    # This makes a dropdown selection list of all the attendees (to add to an event)
    def list_attendees(self):
        alist = []
        for x in self.em.attendees:
            alist.append(f"{x.lastname}, {x.firstname}")
        list_items = Variable(value=alist)
        self.listbox_attendees = Listbox(self.frame, width=30, height=len(alist), listvariable=list_items)
        self.listbox_attendees.bind('<<ListboxSelect>>', self.items_selected)
        self.listbox_attendees.pack()
        self.button_list_attendees["state"] = "disabled"
        self.button_list_attendees_going["state"] = "normal"
        self.is_add_attendees_dropdown = True
        if self.is_current_attendees_dropdown:
            self.listbox_attendees_going.destroy()
            self.is_current_attendees_dropdown = False

    # When selected an attendee in event dropdown list
    def items_selected(self, event):
        self.button_list_attendees["state"] = "normal"

        # get all selected indices
        selected_indices = self.listbox_attendees.curselection()
        selected_langs = ",".join([self.listbox_attendees.get(i) for i in selected_indices])
        self.em.add_event_attendee(self.em.events[self.current_event], self.em.attendees[selected_indices[0]])
        # # get selected items
        # msg = f'You selected: {selected_langs}'
        # # self.label8 = Label(self.frame, text=selected_indices, font=(self.font, self.fontsize))
        # # self.label8.pack()
        self.listbox_attendees.destroy()
        # print(self.em.event_attendees[len(self.em.event_attendees)-1])
