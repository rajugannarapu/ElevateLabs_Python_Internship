# todo.py

# File to store tasks
TASK_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from the file into a list."""
    try:
        with open(TASK_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    """Save tasks from the list into the file."""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\n✅ No tasks found!\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!\n")
    else:
        print("⚠️ Task cannot be empty!\n")


def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"🗑️ Task '{removed}' removed successfully!\n")
            else:
                print("⚠️ Invalid task number!\n")
        except ValueError:
            print("⚠️ Please enter a valid number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
