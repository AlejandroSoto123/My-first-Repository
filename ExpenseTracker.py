expenses = []

def add_expense():
    description = input("Enter expense description: ")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid. Enter a valid amount.")

    expenses.append((description, amount))
    print("Expense added .")

def display_expenses():
    if not expenses:
        print("No expenses to put.")
    else:
        print("List of expenses:")
        for i, expense in enumerate(expenses, 1):
            description, amount = expense
            print(f"{i}. Description: {description}, Amount: {amount}")

def calculate_total_expenses():
    total = sum(amount for _, amount in expenses)
    print(f"Total expenses: {total}")

while True:
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Calculate Total Expenses")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        display_expenses()
    elif choice == "3":
        calculate_total_expenses()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid choice (1-4).")
