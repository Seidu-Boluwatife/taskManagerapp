import json
from json.decoder import JSONDecodeError
from datetime import datetime, timedelta
from storage import save_archived_task

from model import Task

class TaskTracker:

    def __init__(self,):
        # Initial task list (empty)
        self.tasks = []
        self.name = "lingerie"
        self.welcome_msg = "Welcome to Your No'1 Personal Task Tracker"
        self.load_tasks()

    def add_task(self, name, title, description, due_date, priority):
        task = Task(
            task_id=len(self.tasks)+1,
            user=name.lower(),
            title=title.lower(),
            desc=description,
            due=due_date.isoformat(),
            priority=priority,
            created_at=datetime.now().isoformat()
        )
        # task = {
        #     "title": title,
        #     "due_date": due_date,
        #     "priority": priority,
        #     "status": "Pending"
        # }

        self.tasks.append(task.__json__())
        self.save_tasks()
        # self.display_task()

    def display_task(self, name):
        the_task = []
        for task in self.tasks:
            if task.get("username") == name.lower():
                a_task = task.copy()
                a_task["due_date"] = a_task["due_date"][:-9]
                the_task.append(a_task)
        return the_task

    # Function to remove task
    def remove_task(self, task_id):
        index = None
        if 1 <= task_id <= len(self.tasks):
            for index, task in enumerate(self.tasks):
                if task["id"] == task_id:
                    break
            if isinstance(index, int):
                removed = self.tasks.pop(index)
                self.save_tasks()
                return removed
            else:
                return False
        else:
            return False



    # Update Task
    def mark_task(self, task_id):
        task = [task for task in self.tasks if task.get('id') == task_id][0]
        task['status'] = 'Done'
        self.save_tasks()
        # self.load_tasks()
        
        
    def change_date(self, task_id, date):
        task = [task for task in self.tasks if task.get('id') == task_id][0]
        task["due_date"] = date.isoformat()
        self.save_tasks()
        
    
    def change_priority(self, task_id, priority):
        task = [task for task in self.tasks if task.get('id') == task_id][0]
        task["priority"] = priority
        self.save_tasks()


    # load task
    def load_tasks(self, filename="tasks.json"):
        # global tasks  # allow updating the tasks list
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
            print("📁 Tasks loaded successfully.")
        except FileNotFoundError:
            print("🆕 No saved tasks found. Starting fresh.")
        except JSONDecodeError:
            self.tasks = []


    # save task
    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(self.tasks, f, indent=4)
        # print("✅ Task saved.")
        # self.load_tasks()


    # Search task by task name
    def search_tasks(self, task_name: str) -> list:
        found = []
        for task in self.tasks:
            if task_name.lower() in task.get("title"):
                found.append(task)
        return found
    
    #Archive task greater tan 30 days 

    def archive_old_tasks(self):
        new_tasks = []
        for task in self.tasks:
            created = datetime.fromisoformat(task.get("created_at", datetime.now().isoformat()))
            if datetime.now() - created >= timedelta(days=30) and task.get("status") != "Done":
                print(f"📦 Archiving task: {task['title']}")
                save_archived_task(task)
            else:
                new_tasks.append(task)

        self.tasks = new_tasks
        self.save_tasks()