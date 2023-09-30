class Event(object):
    def __init__(self, val: dict):
        self.__name = val["Name"]
        self.__date = val["Date"]
        self.__start_time = val["StartTime"]
        self.__location = val["Location"]
        self.__duration = val["Duration"]

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    @property
    def start_time(self):
        return self.__start_time

    @property
    def location(self):
        return self.__location

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return "Event: {}\nDate: {}\nStart time: {}\nDuration: {} hours\nLocation: {}"\
            .format(self.name, self.date, self.start_time, self.duration, self.location)