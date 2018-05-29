import datetime


class StorageManager:

    def __init__(self, projects=None, items=None):
        self.projects = projects if projects is not None else []
        self.items = items if items is not None else []

    def new_item(self, title, tier=0):
        self.items.append(Item(title, tier))

    def delete_item(self, item):  # TODO implement a proper delete function
        del item                  # TODO find a way to delete specific items

    def __repr__(self):
        rep = ""
        for idx, item in enumerate(self.items):
            rep += ("[{}] {}".format(idx + 1, item))
        return rep


class Item:
    def __init__(self, title, tier=0):
        self.title = title
        self.tier = tier if tier is not 0 else 0
        self.date_of_creation = datetime.date.today()

    def __repr__(self):
        return str(self.title)

    def __delete__(self, instance):  # TODO how to: class destructor
        del self

    def change_title(self, new_title):
        self.title = new_title

    def change_tier(self, new_tier=0):
        self.tier = new_tier if new_tier is not 0 and 0 <= new_tier <= 3 else 0


