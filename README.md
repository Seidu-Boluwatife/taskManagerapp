# taskManagerapp
Task Manager CLI
A sleek and interactive command-line task manager built with Python.
Keep your productivity in check with features like task creation, search, archiving, and more — all from your terminal. 🧠✨

📚 What You Can Do
🆕 Add tasks with title, description, due date, and priority

. View all current tasks

. Search tasks by name

. Mark tasks as done

. Update task priority or due date

. Delete tasks

. Auto-archive old tasks after 30 days

. All tasks saved to tasks.json (no database needed!)

 Project Structure


taskManagerProject/
├── cli.py          # User-facing command-line interface
├── main.py         # Core task management logic
├── model.py        # Task class definition
├── storage.py      # Archive system
├── tasks.json      #  task storage
└── README.md       # This file
 How to Use
 Requirements
Python 3.x installed on your machine

Run the App
bash
Copy code
python cli.py
You’ll be greeted with:


Welcome to Task Manager!
Enter your name:
Then, use the menu to navigate:

Enter option using the displayed index no

1. Add Task
2. Remove Task
3. View Task
4. Search Tasks
5. Update Task / Mark as Done
6. Archive Old Tasks
7. Exit Program

 Date Input Guide
When adding a task, enter the due date in either format:

dd/mm/yyyy → e.g. 25/12/2025

dd/mm/yy → e.g. 25/12/25

 The date must be later than today.
 You get 3 attempts, after which the input process restarts.

 How Archiving Works
Every time you choose Archive Old Tasks, the system will:

 Find tasks older than 30 days
 Check if they're not marked as Done
 Move them to archive.json
 Clean them from your active task list (tasks.json)


🧪 Testing Archive Feature
To test archiving manually:

Edit a task’s "created_at" field in tasks.json to be over 30 days ago

Make sure its "status" is not "Done"

Run the program and choose Option 6 (Archive Old Tasks)

The task should move to archive.json

💾 Data Storage
File	Purpose
tasks.json	Stores your current to-dos
archive.json	Stores archived/expired tasks

Both files are in human-readable JSON format — no DB setup required.

