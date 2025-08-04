
from datetime import datetime


class Task:
    def __init__(self, task_id, user, title, desc, due, priority,created_at=None):
        self.id: int = task_id
        self.username: str = user
        self.title: str = title
        self.desc: str = desc
        self.due_date: str = due
        self.priority: str = priority
        self.status: str = "Pending"
        self.archived: bool = False
        self.created_at = created_at or datetime.now().isoformat()
    def __str__(self):
        return f"i am a task created by {self.username}"


    def __json__(self):
        return {
            "id": self.id,
            "username": self.username,
            "title": self.title,
            "description": self.desc,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
            "archived": self.archived,
            "created_at": self.created_at
        }

# task = Task(
#             user="Dickson",
#             title="title",
#             desc="description",
#             due="due_date",
#             priority="priority",
#         )
# print(task.__dict__)
# print(task)
