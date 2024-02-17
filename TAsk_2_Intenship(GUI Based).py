import tkinter as tk
from tkinter import messagebox
import json

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file)

def add_transaction():
    category = category_entry.get()
    amount = float(amount_entry.get())
    is_income = income_var.get()
    transactions.append({"category": category, "amount": amount, "is_income": is_income})
    save_transactions(transactions)
    messagebox.showinfo("Success", "Transaction added successfully!")
    refresh_display()

def calculate_budget():
    total_income = sum(transaction["amount"] for transaction in transactions if transaction["is_income"])
    total_expenses = sum(transaction["amount"] for transaction in transactions if not transaction["is_income"])
    remaining_budget = total_income - total_expenses
    messagebox.showinfo("Budget Calculation", f"Total Income: {total_income}\nTotal Expenses: {total_expenses}\nRemaining Budget: {remaining_budget}")

def analyze_expenses():
    categories = {}
    for transaction in transactions:
        if not transaction["is_income"]:
            category = transaction["category"]
            amount = transaction["amount"]
            categories[category] = categories.get(category, 0) + amount
    analysis_text = "\n".join([f"{category}: {amount}" for category, amount in categories.items()])
    messagebox.showinfo("Expense Analysis", analysis_text)

def refresh_display():
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    income_var.set(False)

transactions = load_transactions()

root = tk.Tk()
root.title("Budget Tracker")

# Add transaction section
add_frame = tk.Frame(root)
add_frame.pack(pady=20)

category_label = tk.Label(add_frame, text="Category:")
category_label.grid(row=0, column=0, padx=10)
category_entry = tk.Entry(add_frame)
category_entry.grid(row=0, column=1, padx=10)

amount_label = tk.Label(add_frame, text="Amount:")
amount_label.grid(row=0, column=2, padx=10)
amount_entry = tk.Entry(add_frame)
amount_entry.grid(row=0, column=3, padx=10)

income_var = tk.BooleanVar()
income_checkbox = tk.Checkbutton(add_frame, text="Income", variable=income_var)
income_checkbox.grid(row=0, column=4, padx=10)

add_button = tk.Button(add_frame, text="Add Transaction", command=add_transaction)
add_button.grid(row=0, column=5, padx=10)

# Budget calculation section
calculation_button = tk.Button(root, text="Calculate Budget", command=calculate_budget)
calculation_button.pack()

# Expense analysis section
analysis_button = tk.Button(root, text="Analyze Expenses", command=analyze_expenses)
analysis_button.pack()

root.mainloop()
