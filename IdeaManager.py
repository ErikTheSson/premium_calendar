import datetime


class IdeaManager:
    # TODO change to IdeManager, so each manager stores individually

    def __init__(self, projects=None, idea=None):
        self.projects = projects if projects is not None else []
        self.ideas = idea if idea is not None else []

    def new_idea(self, title, tier=0):
        self.ideas.append(Idea(title, tier))

    def store_ideas(self):  # TODO implement store_ideas
        pass

    def store_idea(self):   # TODO implement store_idea
        pass

    def __repr__(self):
        rep = ""
        for idx, idea in enumerate(self.ideas):
            rep += ("[{}] {}".format(idx + 1, idea))
        return rep


class Idea:
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


