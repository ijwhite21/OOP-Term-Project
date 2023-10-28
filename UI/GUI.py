from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from classes.Event_Manager import EventManager
from classes.Contact import Contact

"""
The Gui class handles all of the visuals via the tkinter library. 
It generally works by calling the EventManager functions via aggregation whenever a button is pressed etc.

NOTE: tkinter generally works by creating frames (areas on the screen to put "stuff" in) and then defining widgets (buttons, labels, text entry boxes etc).
The widgets do not appear on the screen just from defining them. Once you call the pack() function for each widget, it will place it on the screen.
The pack() function will place it in the next available spot while grid() can specify rows and columns where the widget can go,
In this implementation, pack() is used for simplicity, but grid() may be implemented in the future to allow for more control over the appearance.

Below is a quick example of creating a tkinter widget. The first line defines it using the Button() function built into tkinter.
The first argument specifies which frame to place the button in. Remember, frames are rectangular areas on the screen that we put "stuff" in.
The "command=" part simply tells the program which function to call when the button is pressed.

example

    self.my_button = Button(self.my_frame, text="My Button", font=(self.font, self.fontsize), command=self.my_button_function)
    self.my_button_add_contact.pack()
"""
class Gui:
    # Gui constructor. NOTE: an Event_Manager object is passed into the constructor. This is so that the Gui class can pass data into it.
    def __init__(self, eventmanager):
        #establish font
        self.fontsize: int = 18
        self.font: str = 'Arial'

        # We've instantiated an event manager in main. We then aggregate it onto the Gui so that it can receive form submissions etc
        self.em: EventManager = eventmanager

        # This variable is used to create an Event_Attendee object later on
        self.current_event: int = 0

        # These are used to destroy the dropdown lists on the same page
        self.is_current_attendees_dropdown: bool = False
        self.is_add_attendees_dropdown: bool = False

        #This adds the tk functionality to the Gui class
        self.root = Tk()
        # this is where a lot of the visuals can be declared (kinda like CSS) (inbetween the dotted lines)
        # This sets the text in the window border
        self.root.title("OOP TERM PROJECT")
        # This line sets the resolution
        self.root.geometry("640x480")
        # This is part of the closing function (whenever you ex out of the program)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # create the side bar (the frame on the left of the screen with the buttons: "Create Contact", "Create Event", "Display Contacts", "Display Events")
        self.create_side_bar()

        # this is the loop that refreshes the GUI screen
        self.root.mainloop()

    # create the side bar (the frame on the left of the screen with the buttons: "Create Contact", "Create Event", "Display Contacts", "Display Events")
    def create_side_bar(self):
        # create the frame for the side buttons "Create Contact", "Create Event", etc (this will always be on the screen)
        self.sidebuttons = LabelFrame(self.root, padx=2, pady=10)
        # this pack() function is what places the frame on the screen
        self.sidebuttons.pack(side="left", expand=False, fill="both")

        # add_contact button
        # Every widget (buttons, text inputs, labels etc) is defined first, then placed on the screen using pack()

        # The first argument is which frame to place the button in which in this case is self.sidebuttons which was defined above
        # "command=" is saying that whenever the button is clicked on, the self.contact_screen function will be called
        # NOTE: that self.contact_screen does not have "()" at the end. We don't want to call the function at this time, only link it to the button.
        self.button_add_contact = Button(self.sidebuttons, text="Create Contact", font=(self.font, self.fontsize),
                                         command=self.contact_screen)
        # We defined the button above, now using pack() we will place it in the next available spot in the frame "sidebuttons"
        # In future implementations, pack() may be replaced by grid() as you can specify which row and column to place the button.
        # pack() was used to save time for now
        self.button_add_contact.pack()

        # add_event button
        self.button_add_event = Button(self.sidebuttons, text="Create Event", font=(self.font, self.fontsize),
                                       command=self.event_screen)
        self.button_add_event.pack()

        # display contacts button
        self.button_display_contacts = Button(self.sidebuttons, text="Display Contacts",
                                              font=(self.font, self.fontsize), command=self.display_contacts)
        self.button_display_contacts.pack()

        # display events button
        self.button_display_events = Button(self.sidebuttons, text="Display Events", font=(self.font, self.fontsize),
                                            command=self.display_events)
        self.button_display_events.pack()

        # establish the frame that will house each type of form. this will be cleared, then repopulated will the selected form or "state"
        # NOTE: This frame will house everything on the screen that isn't on the sidebar on the left
        self.frame = LabelFrame(self.root, padx=0, pady=10)
        self.frame.pack(side="right", expand=True, fill="both")

    # This function is called whenever you try to close the window
    def on_closing(self):
        # the line below is commented out for convenience. It simply asks if you're sure you want to quit upon exing out
        # if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            # close the program
            self.root.destroy()

    # This clears the right-hand frame of all widgets. This is called every time the menu changes to another screen
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # this function disables the button you have clicked (mainly to mark which page you are currently on)
    # a string is passed in to check which button has been pressed
    def button_state(self, button: str):
        # the buttons have 2 states: "normal" and "disabled"
        # "disabled" will gray it out and make you unable to click it

        # this enables all buttons
        self.button_add_contact["state"] = "normal"
        self.button_add_event["state"] = "normal"
        self.button_display_contacts["state"] = "normal"
        self.button_display_events["state"] = "normal"

        # this will then check and disable whichever button was pressed
        if button == "add_contact":
            self.button_add_contact["state"] = "disabled"

        elif button == "add_event":
            self.button_add_event["state"] = "disabled"

        elif button == "display_contacts":
            self.button_display_contacts["state"] = "disabled"

        elif button == "display_events":
            self.button_display_events["state"] = "disabled"



    # This function creates the "Create Contact" screen
    def contact_screen(self):
        # before creating the screen, we need to clear whatever is there in the frame
        self.clear_frame()

        # this will disable the "add_contact" button on the screen since we have just clicked on it
        self.button_state("add_contact")

        # these are label definitions followed by text entry box definitions for each attribute
        # this label will simply say 'First Name' above the text box
        self.label_firstname = Label(self.frame, text="First Name", font=(self.font, self.fontsize))
        # this text box is for entering the first name
        self.firstname_entry = Entry(self.frame)
        self.label_lastname = Label(self.frame, text="Last Name", font=(self.font, self.fontsize))
        self.lastname_entry = Entry(self.frame)
        self.label_email = Label(self.frame, text="Email", font=(self.font, self.fontsize))
        self.email_entry = Entry(self.frame)
        self.label_department = Label(self.frame, text="Department", font=(self.font, self.fontsize))
        self.department_entry = Entry(self.frame)
        self.label_title = Label(self.frame, text="Title", font=(self.font, self.fontsize))
        self.title_entry = Entry(self.frame)
        self.label_phone = Label(self.frame, text="Phone #", font=(self.font, self.fontsize))
        self.phone_entry = Entry(self.frame)
        self.label_building = Label(self.frame, text="Building", font=(self.font, self.fontsize))
        self.building_entry = Entry(self.frame)

        # the pack() function will put the Gui component in the next available
        # space on the screen. It's a quick fix. There's better looking ways to
        # do it where you can specify padding etc.
        self.label_firstname.pack()
        self.firstname_entry.pack()
        self.label_lastname.pack()
        self.lastname_entry.pack()
        self.label_email.pack()
        self.email_entry.pack()
        self.label_department.pack()
        self.department_entry.pack()
        self.label_title.pack()
        self.title_entry.pack()
        self.label_phone.pack()
        self.phone_entry.pack()
        self.label_building.pack()
        self.building_entry.pack()

        # pressing this button in the Gui will create a new contact with the entered info from the above text boxes
        self.button = Button(self.frame, text="Create", font=(self.font, self.fontsize), command=self.form_submission_contact)
        self.button.pack()

    # This function is called whenever you click the "Create" button on the "Create contact" screen
    def form_submission_contact(self):
        """
        We are collecting the input from each text field and creating a dictionary.
        This is then passed into the event managers add_contact method which
        passed the same dictionary into the constructor of the Contact class
        """
        a = {
            "FirstName": self.firstname_entry.get(),
            "LastName": self.lastname_entry.get(),
            "UID": self.em.contactUID,
            "EmailAddress": self.email_entry.get(),
            "Dept": self.department_entry.get(),
            "Title": self.title_entry.get(),
            "Phone": self.phone_entry.get(),
            "Building": self.building_entry.get()
            }

        # add a new contact to the event manager's list of contacts using the dictionary data
        self.em.add_contact(a)

        # clear the frame and print on the screen "Contact Added!"
        self.clear_frame()
        self.label_contact = Label(self.frame, text="Contact Added!\n", font=('Arial', 18))
        self.label_contact.pack()

        # prompt user to add another contact if they want
        self.button_add_another_contact = Button(self.frame, text="Create Another?", font=(self.font, self.fontsize),
                                       command=self.contact_screen)
        self.button_add_another_contact.pack()

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

        # pressing this button in the Gui will create a new contact with the entered info from the above text boxes
        self.button = Button(self.frame, text="Create", font=(self.font, self.fontsize), command=self.form_submission_event)
        self.button.pack()

    # This function is called when you click the "Create" button on the "Create Event" screen
    def form_submission_event(self):
        # a dictionary is created with event info then used to create an event
        a = {
            "Name": self.eventname_entry.get(),
            "Date": self.eventdate_entry.get(),
            "UID" : self.em.eventUID,
            "StartTime": self.eventstarttime_entry.get(),
            "Location": self.eventlocation_entry.get(),
            "Duration": self.eventduration_entry.get()
        }

        self.em.add_event(a)

        self.clear_frame()
        self.label_event = Label(self.frame, text="Event Added!\n", font=('Arial', 18))
        self.label_event.pack()

        self.button_add_another_event = Button(self.frame, text="Create Another?", font=(self.font, self.fontsize),
                                                 command=self.event_screen)
        self.button_add_another_event.pack()

    # display all the contacts in a list
    def display_contacts(self):
        self.clear_frame()
        self.button_state("display_contacts")
        alist = []
        # get contacts in the form of a list of first and last names
        for x in self.em.contacts:
            alist.append(f"{x.lastname}, {x.firstname}")
        list_items = Variable(value=alist)
        self.listbox = Listbox(self.frame, height=len(alist), font=(self.font, self.fontsize), listvariable=list_items)
        self.listbox.bind('<<ListboxSelect>>', self.select_contact)
        self.listbox.pack()

    # when a contact is selected from the list to see their info
    def select_contact(self, event):
        # get all selected indices
        selected_indices = self.listbox.curselection()
        # get selected items
        selected_events = ",".join([self.listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_events}'
        # self.label8 = Label(self.frame, text=selected_indices, font=(self.font, self.fontsize))
        # self.label8.pack()
        self.display_contact_single(int(selected_indices[0]))

    #This will display a single contact's info once clicked from the dropdown menu
    def display_contact_single(self, selected_indices):
        self.clear_frame()
        # add a back button
        self.button_back = Button(self.frame, text="Back", font=(self.font, self.fontsize), command=self.display_contacts)
        self.button_back.pack()

        e = self.em.contacts[selected_indices]
        self.label_contactsingle = Label(self.frame, text=e, font=(self.font, self.fontsize), pady=10)
        self.label_contactsingle.pack()

    # display all the events in a list
    def display_events(self):
        self.clear_frame()
        self.button_state("display_events")
        elist = []
        # get contacts in the form of a list of first and last names
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

        self.label_eventsingle = Label(self.frame, text=e, font=(self.font, self.fontsize))
        self.label_eventsingle.pack()

        ## drop down list (unused)
        # variable = StringVar(self.frame)
        # variable.set("")  # default value
        # w = OptionMenu(self.frame, variable, *alist)
        # w.pack()

        # This button will show current attendees for a given event
        self.button_list_attendees_going = Button(self.frame, text="Current Attendees", font=(self.font, self.fontsize), command=self.list_attendees_going)
        self.button_list_attendees_going.pack()
        # add attendee button
        self.button_list_contacts = Button(self.frame, text="Add Attendee", font=(self.font, self.fontsize), command=self.list_contacts)
        self.button_list_contacts.pack()

    # this lists the attendees (contacts) going to a particular events
    def list_attendees_going(self):
        alist = []
        # check who all is going to the event ie event_attendees in the list
        for x in self.em.event_attendees:
            if x.event == self.em.events[self.current_event]:
                alist.append(f"{x.contact.lastname}, {x.contact.firstname}")
        list_items = Variable(value=alist)

        self.listbox_attendees_going = Listbox(self.frame, width=30, height=len(alist), listvariable=list_items)
        self.listbox_attendees_going.pack()
        self.listbox_attendees_going.bind('<<ListboxSelect>>', self.display_event_attendee_single)
        # set the state of the buttons
        self.button_list_attendees_going["state"] = "disabled"
        self.button_list_contacts["state"] = "normal"

        self.is_current_attendees_dropdown = True
        # This will delete the add_attendees dropdown list that would otherwise be in the way
        if self.is_add_attendees_dropdown:
            self.listbox_contacts.destroy()
            self.is_add_attendees_dropdown = False

    # display a single event_attendee object
    def display_event_attendee_single(self, selected_indices):
        selected_indices = self.listbox_attendees_going.curselection()
        # get selected items
        selected_event_attendee = ",".join([self.listbox_attendees_going.get(i) for i in selected_indices])
        self.clear_frame()
        self.button_back = Button(self.frame, text="Back", font=(self.font, self.fontsize),command=self.display_events)
        self.button_back.pack()

        # this will extract the first and lastnames from the selected index in the dropdownlist of attendees (contacts)
        lname = selected_event_attendee.split(", ")[0]
        fname = selected_event_attendee.split(", ")[1]
        e = self.em.events[self.current_event]

        # find the event_attendee object correlating with current event and current attendee (contact) selected
        for x in self.em.event_attendees:
            if x.event == e and x.contact.lastname == lname and x.contact.firstname == fname:
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

    # This makes a dropdown selection list of all the contacts (to add to an event)
    def list_contacts(self):
        alist = []
        for x in self.em.contacts:
            alist.append(f"{x.lastname}, {x.firstname}")
        list_items = Variable(value=alist)
        self.listbox_contacts = Listbox(self.frame, width=30, height=len(alist), listvariable=list_items)
        self.listbox_contacts.bind('<<ListboxSelect>>', self.items_selected)
        self.listbox_contacts.pack()
        self.button_list_contacts["state"] = "disabled"
        self.button_list_attendees_going["state"] = "normal"
        self.is_add_attendees_dropdown = True
        if self.is_current_attendees_dropdown:
            self.listbox_attendees_going.destroy()
            self.is_current_attendees_dropdown = False

    # When selected a contact in event dropdown list
    def items_selected(self, event):
        self.button_list_contacts["state"] = "normal"

        # get all selected indices
        selected_indices = self.listbox_contacts.curselection()
        selected_langs = ",".join([self.listbox_contacts.get(i) for i in selected_indices])
        self.em.add_event_attendee(self.em.events[self.current_event], self.em.contacts[selected_indices[0]])
        # # get selected items
        # msg = f'You selected: {selected_langs}'
        # # self.label8 = Label(self.frame, text=selected_indices, font=(self.font, self.fontsize))
        # # self.label8.pack()
        self.listbox_contacts.destroy()
        # print(self.em.event_attendees[len(self.em.event_attendees)-1])
