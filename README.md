# Coding-Raja-Technologies-Internship

**TASK_1** -- **Command-line to-do list application that allows users to manage tasks.**

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

**TASK 2** --**Console-based budget tracker that allows users to manage their expenses and income.**

File Handling Functions:

**load_transactions():** Reads transactions from a JSON file (transactions.json) and returns them as a list of dictionaries. If the file doesn't exist, it returns an empty list.

**save_transactions(transactions):** Writes the given list of transactions to the JSON file, overwriting its previous content.

**Transaction Management Functions:**

**add_transaction(transactions):** Asks the user for transaction details (category, amount, and whether it's an income), adds the transaction to the list of transactions, and saves the updated list to the file.

**calculate_budget(transactions):** Calculates the total income, total expenses, and remaining budget based on the transactions in the list and prints these values.

**analyze_expenses(transactions):** Analyzes the expenses by summing up the amounts for each category and printing the total amount for each category.

**Main Function (main()):**

Loads the transactions from the file.
Displays a menu with options to add a transaction, calculate the budget, analyze expenses, or exit.
Based on the user's choice, it calls the corresponding function.

**Execution:**

If the script is executed directly (not imported as a module), it calls the main() function to start the budget tracker application.
