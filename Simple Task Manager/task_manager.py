class Task:
    def __init__(self, task_id, title, description, status, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date

def display_menu():
    print("Task Manager Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

def run_task_manager():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    save_tasks(tasks)

def add_task(tasks):
    print("Add a New Task:")
    task_id = input("Enter Task ID: ")
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    status = "Incomplete"
    due_date = input("Enter Due Date: ")

    task = Task(task_id, title, description, status, due_date)
    tasks.append(task)

    print("Task added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return

    print("All Tasks:")
    for task in tasks:
        print(f"Task ID: {task.task_id}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print(f"Status: {task.status}")
        print(f"Due Date: {task.due_date}")
        print()

def mark_task_complete(tasks):
    task_id = input("Enter the Task ID to mark as complete: ")

    for task in tasks:
        if task.task_id == task_id:
            task.status = "Complete"
            print("Task marked as complete!\n")
            return

    print("Task not found.\n")

def save_tasks(tasks):
    import pickle

    with open("tasks.pickle", "wb") as file:
        pickle.dump(tasks, file)

    print("Tasks saved successfully!")

def load_tasks():
    import pickle

    try:
        with open("tasks.pickle", "rb") as file:
            tasks = pickle.load(file)
    except FileNotFoundError:
        tasks = []

    return tasks

if __name__ == "__main__":
    tasks = load_tasks()
    run_task_manager()
