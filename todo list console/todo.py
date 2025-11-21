# To-Do List Console Application
# Programming Foundations with Python Project

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "status": status})
    except FileNotFoundError:
        pass
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for item in tasks:
            file.write(f"{item['task']}|{item['status']}\n")


# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    for idx, item in enumerate(tasks, 1):
        print(f"{idx}. {item['task']}  [{item['status']}]")
    print()


# Add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!\n")


# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted!\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("===============================")
        print("      TO-DO LIST MANAGER       ")
        print("===============================\n")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
