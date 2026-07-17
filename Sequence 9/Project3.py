import os

filename = "ledger.txt"
expenses = []

# Load existing data
if os.path.exists(filename):
    with open(filename, "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            expenses.append([category, float(amount)])

while True:
    print("\n===== Personal Ledger =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Categories")
    print("4. Filter by Maximum Price")
    print("5. View Total Expenses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        expenses.append([category, amount])

        with open(filename, "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nAll Expenses")
            for category, amount in expenses:
                print(f"{category}: ${amount:.2f}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No categories available.")
        else:
            categories = set()

            for category, amount in expenses:
                categories.add(category)

            print("\nCategories")
            for category in categories:
                print(category)

    elif choice == "4":
        try:
            limit = float(input("Show expenses less than or equal to: $"))
        except ValueError:
            print("Invalid number.")
            continue

        found = False

        for category, amount in expenses:
            if amount <= limit:
                print(f"{category}: ${amount:.2f}")
                found = True

        if not found:
            print("No matching expenses found.")

    elif choice == "5":
        total = 0

        for category, amount in expenses:
            total += amount

        print(f"Total Expenses: ${total:.2f}")

    elif choice == "6":
        print("Thank you for using Personal Ledger!")
        break

    else:
        print("Invalid choice. Please try again.")