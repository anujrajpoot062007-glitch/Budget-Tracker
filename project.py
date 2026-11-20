
import pandas as pd

# Empty DataFrame
data = pd.DataFrame(columns=["Type", "Category", "Amount"])

while True:

    print("\n===== BUDGET TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Records")
    print("4. View Budget Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Income
    if choice == "1":

        category = input("Enter income source: ")
        amount = float(input("Enter income amount: "))

        new_data = pd.DataFrame({
            "Type": ["Income"],
            "Category": [category],
            "Amount": [amount]
        })

        data = pd.concat([data, new_data],
                         ignore_index=True)

        print("Income added successfully!")

    # Add Expense
    elif choice == "2":

        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))

        new_data = pd.DataFrame({
            "Type": ["Expense"],
            "Category": [category],
            "Amount": [amount]
        })

        data = pd.concat([data, new_data],
                         ignore_index=True)

        print("Expense added successfully!")

    # View All Records
    elif choice == "3":

        print("\nAll Records:")
        print(data)

    # Budget Report
    elif choice == "4":

        income = data[data["Type"] == "Income"]["Amount"].sum()

        expense = data[data["Type"] == "Expense"]["Amount"].sum()

        balance = income - expense

        print("\n===== BUDGET REPORT =====")
        print("Total Income: ₹", income)
        print("Total Expense: ₹", expense)
        print("Remaining Balance: ₹", balance)

    # Exit
    elif choice == "5":

        print("Thank You for using Budget Tracker!")
        break

    else:
        print("Invalid Choice! Try Again.")
