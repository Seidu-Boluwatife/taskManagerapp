import json

class TaskTracker:

    def __init__(self):
        pass

# Initial task list (empty)
tasks = []

def new_operation():
    load_tasks()
    options = ['Add Task', 'Remove Task', 'View Task', 'Update Task or Mark as done','save and exit']

    for index, option in enumerate(options):
        print(f'{index + 1}. {option}')

    try:
        select_option = int(input("What would you like to do? Please select an option by index number:\n "))
    except ValueError:   # this catches type errors that is if the usere enters a letter rather tan a number since we already declared input as int
        print("Invalid input. Please enter a number.")
        return new_operation(tasks)  # this takes it to the beginning of the function

    if select_option == 1:
        add_task()

    elif select_option == 2:
        remove_task(tasks)

    elif select_option == 3:
        displayTask()

    elif select_option == 4:
        update_task()

    elif select_option == 5:
        save_tasks()
        print("👋 Tasks saved and exiting. Goodbye!")
        return

    else:
        print("Invalid option selected.")
        new_operation()

# Function to add task
# def add_task():
#     print("Enter tasks one by one. Type 'done' when you're finished:")

#     while True:      # this is an infinte loop ,we use tbreak to control the exit
#         new_task = input("→ ").strip()     #.strip removes white spaces

#         if new_task.lower() == 'done':
#             break                           # breaks out of the while loop but continues the function

#         if new_task:
#             tasks.append(new_task)

#     displayTask()


def add_task():
    print("Enter tasks one by one. Type 'done' as task name when you're finished:")

    while True:
        title = input("→ Task name: ").strip()
        if title.lower() == 'done':
            break

        if not title:
            continue

        due_date = input("Due date (dd/mm/yyyy): ").strip()
        priority = input("Priority (L = Low, M = Medium, H = High): ").strip().upper()

        # Normalize priority input
        if priority == 'L':
            priority = 'Low'
        elif priority == 'M':
            priority = 'Medium'
        elif priority == 'H':
            priority = 'High'
        else:
            priority = 'Unknown'

        task = {
            "title": title,
            "due_date": due_date,
            "priority": priority,
            "status": "Pending"
        }

        tasks.append(task)

    displayTask()


#Display Task
# def displayTask():
#     print('\nYour Tasks:')

#     if not tasks:
#         print("No tasks added yet.\n")
#     else:
#         for index, task in enumerate(tasks):
#             print(f"{index + 1}: {task} \n")

#     while True:
#         something_else = input('Would you like to do something else? (y/n): ').strip().lower()

#         if something_else == "y":
#             new_operation(tasks)
#             return                  # return breaks out of the whole function
#         elif something_else == "n":
#             print('👋 Have a productive day.')
#             return
#         else:
#             print("Invalid input. Try again.")
#             return

def displayTask():
    print('\nYour Tasks:')

    if not tasks:
        print("No tasks added yet.\n")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}: {task['title']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {task['status']}")

    while True:
        something_else = input('Would you like to do something else? (y/n): ').strip().lower()
        if something_else == "y":
            new_operation()
            return
        elif something_else == "n":
            print('👋 Have a productive day.')
            return
        else:
            print("Invalid input. Try again.")
            return

# Function to remove task
def remove_task(all_task):
    try:
        task_num = int(input('Enter the task number you want to delete: '))
        if 1 <= task_num <= len(all_task):
            removed = all_task.pop(task_num - 1)
            print(f"Task '{removed}' deleted successfully.")
        else:
            print("Task number out of range.")
    except ValueError:
        print("Invalid input. Enter a number.")

    while True:
        something_else = input("Would you like to do something else? (y/n): ").strip().lower()

        if something_else == 'y':
            new_operation(tasks)
            return
        elif something_else == 'n':
            print("👋 Have a productive day.")
            return
        else:
            print("Invalid input. Try again.")
            return

# Update Task

def update_task():
    displayTask()
    try:
        task_num = int(input("Enter the task number to update/mark as done: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]

            print("What do you want to update?")
            print("1. Mark as Done")
            print("2. Change Due Date")
            print("3. Change Priority")

            choice = input("Enter option number: ").strip()

            if choice == '1':
                task['status'] = 'Done'
                print("Task marked as done.")
            elif choice == '2':
                task['due_date'] = input("New due date (dd/mm/yyyy): ")
            elif choice == '3':
                new_priority = input("New priority (L/M/H): ").strip().upper()
                if new_priority == 'L':
                    task['priority'] = 'Low'
                elif new_priority == 'M':
                    task['priority'] = 'Medium'
                elif new_priority == 'H':
                    task['priority'] = 'High'
                else:
                    print("Invalid priority.")
            else:
                print("Invalid option.")
        else:
            print("Task number out of range.")
    except ValueError:
        print("Please enter a valid number.")
    
    # Ask for next action
    while True:
        something_else = input("Would you like to do something else? (y/n): ").strip().lower()
        if something_else == 'y':
            new_operation()
            return
        elif something_else == 'n':
            print("👋 Have a productive day.")
            return
        else:
            print("Invalid input. Try again.")
            return


#load task
def load_tasks(filename="tasks.json"):
    global tasks  # allow updating the tasks list
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
        print("📁 Tasks loaded successfully.")
    except FileNotFoundError:
        print("🆕 No saved tasks found. Starting fresh.")



#save task


def save_tasks(filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)
    print("✅ Tasks saved.")


# Entry point
print("\n\nWelcome to Your No'1 Personal Task Tracker")

name = input('Hi, please enter your name: ')
print(f'Welcome {name.title()}')
new_operation()
