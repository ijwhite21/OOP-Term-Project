from tkinter import *
from tkinter import messagebox
from classes.Event_Manager import EventManager
from classes.Attendee import Attendee

class Gui:
    def __init__(self, eventmanager):
        self.fontsize = 18
        self.font = 'Arial'
        self.em = eventmanager
        self.root = Tk()
        # SARA, LOOK HERE
        # this is where a lot of the visuals can be declared (kinda like CSS) (inbetween the dotted lines)
        # This sets the text in the window border
        self.root.title("OOP TERM PROJECT")
        # This line sets the resolution
        self.root.geometry("640x480")
        # This is part of the closing function (whenever you ex out of the program)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        #create the frame for the side buttons "Create Attendee", "Create Event", etc (this will always be here)
        self.sidebuttons = Frame(self.root)
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
        self.frame = Frame(self.root)
        self.frame.pack(side="right", expand=True, fill="both")

        # this is the loop that refreshes the GUI
        self.root.mainloop()

    # This function is called whenever you try to close the window
    def on_closing(self):
        # if messagebox.askyesno(title="Quit?", message="Leaving?... Seriously?"):
            self.root.destroy()

    # This clears the frame of all widgets. This is for switching between different views
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # This function is called whenever you click the "Create" button on the "Create Attendee" screen
    def form_submission_attendee(self):
        # self.root.title("It works")

        # a dictionary is created with attendee info then used to create an attendee
        a = {
            "FirstName": self.firstname_entry.get(),
            "LastName": self.lastname_entry.get(),
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
        self.label_attendee = Label(self.frame, text=self.em, font=('Arial', 18))
        self.label_attendee.pack()
        # print(self.em)

    # This function is called when you click the "Create" button on the "Create Event" screen
    def form_submission_event(self):
        pass

    # This function creates the "Create Attendee" screen
    def attendee_screen(self):
        self.clear_frame()

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

    # This function creates the "Create Event" screen
    def event_screen(self):
        self.clear_frame()

        # these are label definitions followed by text entry box definitions for each attribute
        # this label will simply say 'First Name' above the text box
        self.label_eventname = Label(self.frame, text="Event Name", font=(self.font, self.fontsize))
        # this text box is for entering the first name
        self.eventname_entry = Entry(self.frame)

        # the pack() function will put the Gui component in the next available
        # space on the screen. It's a quick fix. There's better looking ways to
        # do it where you can specify padding etc.
        self.label_eventname.pack()
        self.eventname_entry.pack()

        # pressing this button in the Gui will create a new attendee with the entered info from the above text boxes
        self.button = Button(self.frame, text="Create", font=(self.font, self.fontsize), command=self.form_submission_event)
        self.button.pack()

    # display all the attendees in a list
    def display_attendees(self):
        self.clear_frame()

    # display all the events in a list
    def display_events(self):
        self.clear_frame()