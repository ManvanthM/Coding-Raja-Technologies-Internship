import os
import datetime

# Function to load tasks from a file
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip().split(",")
                tasks.append({
                    "task": task_info[0],
                    "priority": task_info[1],
                    "due_date": task_info[2]
                })
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['priority']},{task['due_date']}\n")

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({
        "task": task_name,
        "priority": priority,
        "due_date": due_date
    })
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def complete_task(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

# Function to display all tasks
def list_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i}. {task['task']} (Priority: {task['priority']}, Due: {task['due_date']}, Completed: {task.get('completed', False)})")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nCOMMANDS:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
