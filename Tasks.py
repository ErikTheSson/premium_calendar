class TaskManager:
    """
    Manager for task objects
    """
    def __init__(self, tasks=None,important_tasks=None,
                 timed_tasks=None, mits=None):
        """

        :param tasks: list of task objects
        :param important_tasks: list of task objects with task.important = true
        :param timed_tasks: list of task timed_task objects
        :param mits: list of task objects with mit = true
        """
        self.tasks = tasks if tasks is not None else []
        self.important_tasks = important_tasks \
                            if important_tasks is not None else[]
        self.timed_tasks = timed_tasks if timed_tasks is not None else []
        self.mits = mits if mits is not None else []

    def add_task(self, task, important=False, mit=False, subtasks=None):
       """
       creates a new task object and adds it to the list
        tasks/important tasks/mits

       :param task: string
       :param important: bool
       :param mit: bool
       :param subtasks: list of task objects
       """

       if important:
            self.important_tasks.append(Task(task, important, mit, subtasks))

        else:
        self.tasks.append(Task(task, important, mit, subtasks))

        if mit:
            self.mits.append(Task(task, important, mit, subtasks))

    def add_timed_task(self, task, deadline, important=False,
                 mit=False, subtasks=None):

        if important:
            self.important_tasks.append(TimedTask(task, deadline,
                                                  important, mit,
                                                  subtasks))

        else:
            self.timed_tasks.append(TimedTask(task, deadline,
                                                  important, mit,
                                                  subtasks))
        if mit:
            self.mits.append(TimedTask(task, deadline,
                                        important, mit,
                                        subtasks))


class Task:
    """

    """
    def __init__(self, task, important=False, mit=False, subtasks=None):
        """

        :param task: string
        :param important: bool
        :param mit: bool
        :param subtasks: list of task objects
        """
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
        """

        :return:
        """
        self.important = True

    def make_mit(self):
        """

        :return:
        """
        self.mit = True

    def make_not_important(self):
        """

        :return:
        """
        self.important = False

    def make_not_mit(self):
        """

        :return:
        """
        self.mit = False

    def add_subtask(self, subtask):
        """

        :param subtask:
        :return:
        """
        self.subtasks.append(subtask)
        self.completion_goal += 1

    def check_completion(self):
        """

        :return:
        """
        if self.completion_rate == self.completion_goal:
            return True
        else:
            return False

    def set_completion_goal(self):
        """

        :return:
        """
        all_tasks = 1
        all_tasks += self.get_task_count()

        self.completion_goal = all_tasks

    def get_task_count(self):
        """

        :return:
        """
        task_counter = 0
        for tasks in self.subtasks:
            task_counter += 1

        return task_counter

    def __repr__(self):
        """

        :return:
        """
        output = "{}, {} of {}\n".format(str(self.task),
                                         str(self.completion_rate),
                                         str(self.completion_goal))
        for task in self.subtasks:
            output += task.__repr__()

        return output


class TimedTask(Task):
    """

    """
    def __init__(self, task, deadline, important=False,
                 mit=False, subtasks=None):
        super().__init__(task, important, mit, subtasks)
        self.deadline = deadline

    def change_deadline(self, deadline):
        """

        :param deadline:
        :return:
        """
        self.deadline = deadline

    def __repr__(self):
        """

        :return:
        """
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