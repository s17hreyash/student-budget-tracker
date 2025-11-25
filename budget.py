from storage import save_data


def set_budget(data):
    print("\n--- Set / Update Monthly Budget ---")
    while True:
        amount = input("Enter monthly budget amount (in ₹): ")
        try:
            amount = float(amount)
            if amount < 0:
                print("Budget cannot be negative. Try again.")
                continue
            data["budget"] = amount
            save_data(data)
            print(f"Budget set to ₹{amount:.2f}")
            break
        except ValueError:
            print("Please enter a valid number.")
