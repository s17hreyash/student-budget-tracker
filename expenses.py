from storage import save_data


def add_expense(data):
    print("\n--- Add New Expense ---")
    while True:
        amount = input("Enter amount (in ₹): ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    date = input("Enter date (e.g., 2025-11-25 or Today): ")
    category = input("Enter category (e.g., Food, Travel, Study, Subscription, Other): ")
    description = input("Enter short description: ")

    expense = {
        "amount": amount,
        "date": date,
        "category": category.strip() if category else "Other",
        "description": description.strip()
    }

    data["expenses"].append(expense)
    save_data(data)
    print("Expense added successfully!")


def view_expenses(data):
    print("\n--- All Expenses ---")
    expenses = data.get("expenses", [])
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']:.2f} | {exp['date']} | {exp['category']} | {exp['description']}")
