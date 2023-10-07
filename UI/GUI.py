import tkinter as tk
from tkinter import messagebox
from classes.Event_Manager import EventManager
from classes.Attendee import Attendee

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        # SARA, LOOK HERE
        # this is where a lot of the visuals are declared (kinda like CSS) (inbetween the dotted lines)
        #..............................................................................................................
        # VISUALS GO BELOW THIS LINE
        self.root.title("OOP TERM PROJECT")
        # This line sets the resolution
        self.root.geometry("640x480")
        # This is part of the closing function (whenever you ex out of the program)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # these are label definitions followed by text entry box definitions for each attribute
        # this label will simply say 'First Name' above the text box
        self.label_firstname = tk.Label(self.root, text="First Name", font=('Arial', 18))
        # this text box is for entering the first name
        self.firstname_entry = tk.Entry(self.root)
        self.label_lastname = tk.Label(self.root, text="Last Name", font=('Arial', 18))
        self.lastname_entry = tk.Entry(self.root)
        self.label_email = tk.Label(self.root, text="Email", font=('Arial', 18))
        self.email_entry = tk.Entry(self.root)
        self.label_phone = tk.Label(self.root, text="Phone #", font=('Arial', 18))
        self.phone_entry = tk.Entry(self.root)

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
        self.button = tk.Button(self.root, text="Create Attendee", font=('Arial', 18), command=self.form_submission)
        self.button.pack()


        # VISUALS GO ABOVE THIS LINE
        #..............................................................................................................
        # this is the loop that refreshes the GUI
        self.root.mainloop()

    # This function is called whenever you try to close the window
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Leaving?... Seriously?"):
            self.root.destroy()

    # This function is called whenever you click the "Create Attendee" button
    def form_submission(self):
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
        attendee1 = Attendee(a)
        print(attendee1)