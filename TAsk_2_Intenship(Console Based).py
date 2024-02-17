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

def add_transaction(transactions):
    print("Add a new transaction:")
    category = input("Enter category (e.g., Food, Rent, Salary): ")
    amount = float(input("Enter amount: "))
    is_income = input("Is this an income? (y/n): ").lower() == "y"
    transactions.append({"category": category, "amount": amount, "is_income": is_income})
    save_transactions(transactions)
    print("Transaction added successfully!")

def calculate_budget(transactions):
    total_income = sum(transaction["amount"] for transaction in transactions if transaction["is_income"])
    total_expenses = sum(transaction["amount"] for transaction in transactions if not transaction["is_income"])
    remaining_budget = total_income - total_expenses
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Remaining Budget: {remaining_budget}")

def analyze_expenses(transactions):
    categories = {}
    for transaction in transactions:
        if not transaction["is_income"]:
            category = transaction["category"]
            amount = transaction["amount"]
            categories[category] = categories.get(category, 0) + amount
    for category, amount in categories.items():
        print(f"{category}: {amount}")

def main():
    transactions = load_transactions()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Transaction")
        print("2. Calculate Budget")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            calculate_budget(transactions)
        elif choice == "3":
            analyze_expenses(transactions)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
