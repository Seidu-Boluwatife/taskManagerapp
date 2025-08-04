from main import TaskTracker
from datetime import datetime, timedelta

# Entry point
task_coordinator = TaskTracker()

print(task_coordinator.welcome_msg)
name = input('Hi, please enter your name: ')
print(f'Welcome {name.title()}')

def restart_func(condition: bool):
    if condition:
        new_operation()

def take_date():
    due_date = datetime.now()
    for i in range(3):
        user_input = input("Due date (dd/mm/yyyy) or (dd/mm/yy): ").strip()
        try:
            # 
            due_date = datetime.strptime(user_input, "%d/%m/%Y")
            
        except ValueError:
            try:
                # Fallback to 2-digit year
                due_date = datetime.strptime(user_input, "%d/%m/%y")
            except ValueError:
                print("Incorrect date format. Use dd/mm/yyyy or dd/mm/yy.")
                if i == 2:
                    restart_func(True)
                continue
            # restart = True if i == 2 else restart

        if due_date <= datetime.now() - timedelta(days=1):
            print("Date must be later than today.")
            if i == 2:
                restart_func(True)
        else:
            break
    return due_date

def new_operation():
    # load_tasks()
    restart = False
    options = ['Add Task', 'Remove Task', 'View Task', 'Search Tasks', 'Update Task or Mark as done', 'Archive old','Exit program']

    for index, option in enumerate(options):
        print(f'{index + 1}. {option}')

    try:
        select_option = int(input("What would you like to do? Please select an option by index number: "))
    except ValueError:  # this catches type errors that is if the usere enters a letter rather tan a number since we already declared input as int
        print("Invalid input. Please enter a number.")
        return new_operation()  # this takes it to the beginning of the function

    if select_option == 1:
        print("Enter tasks one after another. Type 'done' as task name when you're finished:")
        while True:
            title = input("→ Task name: ").strip()
            if title.lower() == 'done':
                break
            if not title:
                continue

            due_date = take_date()
            # restart_func(restart) # Remember to test with a wrong date
            priority = input("Priority (L = Low, M = Medium, H = High): ").strip().upper()
            prior = {"L": "Low", "M": "Medium", "H": "High"}
            priority = prior.get(priority) if prior.get(priority) is not None else "Unknown"

            description = input("Describe your task: ")
            task_coordinator.add_task(name, title, description, due_date, priority)
            print("Tssk added sucessfully")


            # Normalize priority input
            # if priority == 'L':
            #     priority = 'Low'
            # elif priority == 'M':
            #     priority = 'Medium'
            # elif priority == 'H':
            #     priority = 'High'
            # else:
            #     priority = 'Unknown'

    elif select_option == 2:
        tasks = task_coordinator.display_task(name)
        for i in range(3):
            try:
                task_num = int(input('Enter the task number you want to delete: '))
                removed = task_coordinator.remove_task(tasks[task_num-1]["id"])
                if removed:
                    # removed = all_task.pop(task_num - 1)
                    print(f"Task '{removed['title']}' deleted successfully.")
                else:
                    print("Task number out of range.")
            except ValueError:
                print("Invalid input. Enter a number!!")
                if i == 2:
                    restart_func(True)
            else:
                break

    elif select_option == 3:
        print('\nYour Tasks:')
        tasks = task_coordinator.display_task(name)
        if not tasks:
            print("No tasks added yet.\n")
        else:
            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}: {task['title']} | Description: {task.get('description')} | Due: {task['due_date']} | Priority: {task['priority']}")
        print("-----"*10)

    elif select_option == 4:
        task_name = input("Input some part of the task name: ")
        found = task_coordinator.search_tasks(task_name)
        for index, task in enumerate(found):
            print(
                f"{index + 1}: {task['title']} | Description: {task.get('description')} | Due: {task['due_date']} | Priority: {task['priority']}")
        print("-----"*10)


    elif select_option == 5:
        tasks = task_coordinator.display_task(name)
        for index, task in enumerate(tasks):
            print(
                f"{index + 1}: {task['title']} | Description: {task.get('description')} | Due: {task['due_date']} | Priority: {task['priority']}")

        try:
            task_num = int(input("Enter the task number to update/mark as done: "))
            print("What do you want to update?")
            print("1. Mark as Done")
            print("2. Change Due Date")
            print("3. Change Priority")

            if 1 <= task_num <= len(tasks):
                task = tasks[task_num - 1]

                choice = input("Enter option number: ").strip()

                if choice == '1':
                    task_coordinator.mark_task(task.get("id"))
                    print("Task marked as done.")
                elif choice == '2':
                    new_due_date = take_date()
                    task_coordinator.change_date(task.get("id"), new_due_date)
                elif choice == '3':
                    new_priority = input("New priority (L/M/H): ").strip().upper()
                    prior = {"L": "Low", "M": "Medium", "H": "High"}
                    priority = prior.get(new_priority) if prior.get(new_priority) is not None else "Unknown"
                    task_coordinator.change_priority(task.get("id"), priority)
                else:
                        print("Invalid option.")
            else:
                print("Task number out of range.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif select_option == 6 :
        task_coordinator.archive_old_tasks()
        


    elif select_option == 7:
        print("👋 Tasks saved and exiting. Goodbye!")
        exit()

    else:
        print("Invalid option selected.")
        new_operation()

    new_operation()
new_operation()