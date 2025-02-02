# budget_tracker.py

def get_monthly_income():
    """Prompt the user for monthly income."""
    while True:
        try:
            income = float(input("Enter your monthly income: $"))
            if income >= 0:
                return income
            else:
                print("Income must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_expense(expenses):
    """Add an expense to a specific category."""
    category = input("Enter the expense category: ")
    while True:
        try:
            amount = float(input(f"Enter the amount for {category}: $"))
            if amount >= 0:
                expenses[category] = expenses.get(category, 0) + amount
                print(f"Added ${amount:.2f} to {category}.")
                break
            else:
                print("Amount must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_summary(income, expenses):
    """Display a summary of the budget."""
    total_expenses = sum(expenses.values())
    remaining_budget = income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income: ${income:.2f}")
    print("Expenses:")
    for category, amount in expenses.items():
        percentage = (amount / income) * 100 if income > 0 else 0
        print(f"  {category}: ${amount:.2f} ({percentage:.1f}%)")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

def main():
    """Main function for the budget planner."""
    print("Welcome to the Budget Planner and Expense Tracker!")
    income = get_monthly_income()
    expenses = {}

    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. View budget summary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_summary(income, expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
