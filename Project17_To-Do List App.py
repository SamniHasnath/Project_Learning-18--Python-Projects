# To-Do List App (Command Line Version)

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as f:
            for line in f:
                task, done = line.strip().split("|")
                tasks.append({"task": task, "done": done == "True"})
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(f"{task['task']}|{task['done']}\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")


def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")


def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the app
main()
