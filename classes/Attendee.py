class Attendee(object):
    def __init__(self, val: dict):
        self.__lastname = val["LastName"]
        self.__firstname = val["FirstName"]
        if "MiddleName" in val:
            self.__middlename = val["MiddleName"]
        self.__email = val["EmailAddress"]
        self.__department = val["Dept"]
        self.__title = ""
        self.__title = val["Title"]
        self.__phone = val["Phone"]
        self.__building = val["Building"]
        if "POBOX" in val:
            self.__mailcode = val["POBOX"]

    @property
    def lastname(self):
        return self.__lastname

    @property
    def firstname(self):
        return self.__firstname

    @property
    def email(self):
        return self.__email

    @property
    def department(self):
        return self.__department

    @property
    def title(self):
        return self.__title

    @property
    def phone(self):
        return self.__phone

    @property
    def building(self):
        return self.__building

    @property
    def mailcode(self):
        return self.__mailcode

    def __str__(self):
        return "{} {}\nTitle: {}\nEmail: {}\nDepartment: {}\nPhone: {}\n"\
               "Building: {}\n".format(self.firstname,
                                                   self.lastname,
                                                   self.title,
                                                   self.email,
                                                   self.department,
                                                   self.phone,
                                                   self.building)