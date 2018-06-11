import CalendarEntry

from CalendarEntry import CalendarEntry


class Calendar:
    """
    Calendar class to display in the GUI
    """
    def __init__(self, name, entries=None, color=None, rss=None):
        """
        initialize function for the calendar object

        :param name: string
        :param entries : list[calender entry object]
        :param color:
        :param rss:
        """
        self.name = name
        self.entries = entries if entries is not None else []
        self.color = color
        self.rss = rss if rss is not None else None

    def add_calendar_entry(self, title,
                           date, time,
                           color, location=None,
                           deadline=False):
        """
        Creates new calendar entry object and adds it to calender entries list

        :param title: string
        :param date:  datetime date
        :param time:
        :param color:
        :param location: string
        :param deadline:
        :return:
        """
        self.entries.append(CalendarEntry(title, date, time,
                                          color, location))

    def delete_calendar_entry(self, entry):
        """
        deletes the given calendar entry

        :param entry: calenderentry
        :return:
        """
        del entry

    def change_color(self, color):
        """
        changes the color of all entries of the calendar object

        :param color:
        :return:
        """
        self.color = color
        for entry in self.entries:
            entry.change_color(color)


