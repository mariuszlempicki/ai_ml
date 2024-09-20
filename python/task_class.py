class Task:
    def __init__(self,
                 description: str,
                 assignee: str,
                 due_date: str,
                 priority: str,
                 tags: list,
                 time_logged: float = 0,
                 is_complete: bool = False,
                 comments: bool = []):
        self.description = description
        self.assignee = assignee
        self.due_date = due_date
        self.priority = priority
        self.tags = tags
        self.time_logged = time_logged
        self.is_complete = is_complete
        self.comments = comments

    def edit_description(self):
        pass

    def mark_as_complete(self):
        pass

    def add_comment(self):
        pass
