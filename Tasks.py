class TaskManager:
    def __init__(self, tasks=None,important_tasks=None,
                 timed_tasks=None, mits=None):
        self.tasks = tasks if tasks is not None else []
        self.important_tasks = important_tasks \
                            if important_tasks is not None else[]
        self.timed_tasks = timed_tasks if timed_tasks is not None else []
        self.mits = mits if mits is not None else []

    def add_task(self, task):
        if task.important():
            self.important_tasks.append(task)
        else:
            self.tasks.append(task)
        if task.mit:
            self.mits.append(task)

    def add_timed_task(self, timed_task):
        self.add_task(timed_task)
        self.timed_tasks.append(timed_task)


class Task:
    # task is a the action that is needed to complete the task,
    # formated as a string
    # subtasks is a list of task-objects
    def __init__(self, task, important=False, mit=False, subtasks=None):
        self.mit = False if mit is False else True
        self.important = False if important is False else True
        self.task = [task]
        self.subtasks = []
        self.completion_goal = 1
        self.completed = False
        self.completion_rate = 0
        for task in subtasks:
            self.subtasks.append(task)
        self.set_completion_goal()

    def make_important(self):
        self.important = True

    def make_mit(self):
        self.mit = True

    def make_not_important(self):
        self.important = False

    def make_not_mit(self):
        self.mit = False

    def add_subtask(self, subtask):  # subtask is an task-object
        self.subtasks.append(subtask)
        self.completion_goal += 1

    def check_completion(self):
        if self.completion_rate == self.completion_goal:
            return True
        else:
            return False

    def set_completion_goal(self):
        all_tasks = 1
        all_tasks += self.get_task_count()

        self.completion_goal = all_tasks

    def get_task_count(self):
        task_counter = 0
        for tasks in self.subtasks:
            task_counter += 1

        return task_counter

    def __repr__(self):
        output = "{}, {} of {}\n".format(str(self.task),
                                         str(self.completion_rate),
                                         str(self.completion_goal))
        for task in self.subtasks:
            output += task.__repr__()

        return output


class TimedTask(Task):
    def __init__(self, task, deadline, important=False,
                 mit=False, subtasks=None):
        super().__init__(task, important, mit, subtasks)
        self.deadline = deadline

    def change_deadline(self, deadline):
        self.deadline = deadline

    def __repr__(self):
        output = "{}, {} of {}".format(str(self.task),
                                         str(self.completion_rate),
                                         str(self.completion_goal))
        if self.deadline:
            output += "{}\n".format(str(self.deadline))
        else:
            output += "\n"

        for task in self.subtasks:
            output += task.__repr__()

        return output