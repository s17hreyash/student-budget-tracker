from storage import load_data
from budget import set_budget
from expenses import add_expense, view_expenses
from reports import view_summary


def main_menu():
    data = load_data()

    while True:
        print("\n==============================")
        print("Student Budget Tracker")
        print("==============================")
        print("1. Set / Update Monthly Budget")
        print("2. Add Expense")
        print("3. View All Expenses")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            set_budget(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            view_expenses(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
