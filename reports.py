def view_summary(data):
    print("\n--- Budget Summary ---")
    budget = data.get("budget", 0.0)
    expenses = data.get("expenses", [])

    total_spent = sum(exp["amount"] for exp in expenses)
    remaining = budget - total_spent
    remaining = round(remaining, 2)

    if budget > 0:
        used_percent = (total_spent / budget) * 100
    else:
        used_percent = 0.0

    print(f"Monthly Budget : ₹{budget:.2f}")
    print(f"Total Spent    : ₹{total_spent:.2f}")
    print(f"Remaining      : ₹{remaining:.2f}")
    print(f"Used %         : {used_percent:.2f}%")

    print("\nCategory-wise spending:")
    category_totals = {}
    for exp in expenses:
        cat = exp["category"] or "Other"
        category_totals[cat] = category_totals.get(cat, 0.0) + exp["amount"]

    if not category_totals:
        print("No expenses to show.")
    else:
        for cat, amt in category_totals.items():
            print(f"- {cat}: ₹{amt:.2f}")
