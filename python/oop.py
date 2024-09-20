class Task:
    def __init__(self, text, assignee=None, tags=[]):
        self.description = text
        self.assignee = assignee
        self.__tags = tags
        self._comments = []  # 'comments' attribute is protected

    def modify_description(self, new_description):
        self.description = new_description

    def add_comment(self, comment):
        self._comments.append(comment)


class TaskInheritance(Task):
    def __init__(self):
        super().__init__("text")

    def method(self):
        self._comments = []


class Task:
    def __init__(self, text, assignee=None, tags=[]):
        self.description = text
        self.assignee = assignee
        self.tags = tags
        self.comments = []

    @classmethod
    def from_dict(cls, task_dict):
        text = task_dict.get("description")
        assignee = task_dict.get("assignee")
        tags = task_dict.get("tags")

        return cls(text, assignee, tags)


task = Task.from_dict({"description": "Learn Python from dict", "assignee": "Andrzej", "tags": []})
print(task)
