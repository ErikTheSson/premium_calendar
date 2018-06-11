import datetime


class ProjectManager:
    def __init__(self, projects=None,
                 timed_projects=None,
                 current_projects=None):
        self.projects = projects if projects is not None else []
        self.timed_projects = timed_projects \
            if timed_projects is not None else []
        self.current_projects = current_projects \
            if current_projects is not None else []

    def add_project(self, title, tasks=None, active=False, tier=0):
        self.projects.append(Project(title, tasks, active, tier))
        if active:
            self.current_projects.append(Project(title, tasks, active, tier))

    def add_timed_project(self, title,
                          deadline, tasks=None,
                          active=False, tier=0):
        self.timed_projects.append(TimedProject(title, deadline,
                                                tasks, active,
                                                tier))

    def activate_project(self, project):
        project.active = True

    def delete_project(self, project):
        del project

    def new_project_from_storage_item(self, project, storage, storage_item):
        self.projects.append(project)
        if project.active:
            self.current_projects.append(project)
        storage.delete_item(storage_item)

    def store_projects(self):   # TODO implement store_projects
        pass


class Project:
    def __init__(self, title, tasks=None,
                 active=False, tier=0):
        self.title = title
        self.tasks = tasks if tasks is not None else []
        self.active = False if active is False else True
        self.tier = tier if 0 <= tier <= 3 else 0
        self.date_of_creation = datetime.date.today()
        self.completion_rate = 0
        self.completion_step = 0
        self.completion_goal = 0
        self.calc_completion_goal_and_step()
        self.calculate_completion_rate()

    def calc_completion_goal_and_step(self):
        counter = 0
        for task in self.tasks:
            counter += 1
        self.completion_goal = counter
        self.completion_step = 100/self.completion_goal

    def calculate_completion_rate(self):
        self.calc_completion_goal_and_step()
        for task in self.tasks:
            if task.completed:
                self.completion_rate += self.completion_step

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def change_tier(self, tier=0):
        self.tier = tier if 0 <= tier <= 3 else 0

    def add_tasks(self, tasks):
        self.tasks.append(tasks)
        self.calc_completion_goal_and_step()

    def __repr__(self):
        self.calculate_completion_rate()
        out = "{}, {}\n".format(self.title, self.completion_rate)
        for task in self.tasks:
            out = str(task.__repr__()) + "\n"
        return out


class TimedProject(Project):
    def __init__(self, title,
                 deadline, tasks=None,
                 active=False, tier=0):
        super().__init__(title, tasks, active, tier)
        self.deadline = deadline

    def __repr__(self):
        self.calculate_completion_rate()
        out = "{}, {}, {}\n".format(self.title, self.deadline, self.completion_rate)
        for task in self.tasks:
            out = str(task.__repr__()) + "\n"
        return out

