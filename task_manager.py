import json

tasks = {}
task_file = "tasks.json"

def add_task(title):
    task_id = len(tasks) + 1
    tasks[task_id] = {"title": title, "completed": False}
    print(f"Task '{title}' added with ID {task_id}.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"ID: {task_id} | Title: {task['title']} | Status: {status}")

def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task with ID {task_id} deleted.")
    else:
        print(f"No task found with ID {task_id}.")

def mark_task_complete(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"Task with ID {task_id} marked as completed.")
    else:
        print(f"No task found with ID {task_id}.")

def save_tasks():
    with open(task_file, "w") as f:
        json.dump(tasks, f)
    print("Tasks saved to file.")

def load_tasks():
    global tasks
    try:
        with open(task_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = {}

def main():
    load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as complete: "))
                mark_task_complete(task_id)
            except ValueError:
                print("Please enter a valid task ID.")
        elif choice == "5":
            save_tasks()
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
