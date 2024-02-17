# Coding-Raja-Technologies-Internship

Task 1
Importing Modules: The code starts by importing the os and datetime modules. os is used to interact with the operating system (e.g., checking file existence), and datetime is used for working with dates and times.

Function Definitions:

**load_tasks():** This function reads tasks from a file named "tasks.txt" and returns them as a list of dictionaries. Each dictionary represents a task with keys for the task name, priority, due date, and completion status.

**save_tasks(tasks):** This function takes a list of tasks (dictionaries) and writes them back to the "tasks.txt" file. It formats each task as a comma-separated string and writes it to the file.

**add_task(tasks):** This function prompts the user to enter a task name, priority (e.g., high, medium, low), and due date (in the format YYYY-MM-DD). It then adds the task to the list of tasks and saves the updated list to the file.

**remove_task(tasks):** This function prompts the user to enter the index of the task to remove and deletes that task from the list of tasks. It then saves the updated list to the file.

**complete_task(tasks):** This function prompts the user to enter the index of the task to mark as completed and updates the completion status of that task to True. It then saves the updated list to the file.

**list_tasks(tasks):** This function prints a numbered list of all tasks, including their names, priorities, due dates, and completion status.

**Main Function (main()):**

The main() function is the entry point of the program.
It loads tasks from the file using load_tasks() and stores them in a variable named tasks.
It then enters a loop where it repeatedly displays a menu of options to the user and waits for their input.
Based on the user's choice, it calls the corresponding function (add_task(), remove_task(), complete_task(), list_tasks()) to perform the selected action.
The loop continues until the user chooses to exit by selecting option 5.

Execution:

The if __name__ == "__main__": block ensures that the main() function is only executed if the script is run directly (not imported as a module).
When the script is run, the main() function is called, starting the to-do list application.
