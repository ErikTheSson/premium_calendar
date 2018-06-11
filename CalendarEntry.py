class CalendarEntry:
    """
    Class to create CalenderEntries for the Calender Class
    """
    def __init__(self, title, date, time,
                 color, location=None):
        """

        :param title: string
        :param date: datetime date
        :param time:
        :param color:
        :param location: string
        """
        self.title = title
        self.date = date
        self.time = time
        self.color = color
        self.location = location if location is not None else None

    def change_color(self, color):
        self.color = color
