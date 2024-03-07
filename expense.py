import os
import json
from datetime import datetime

# Function to load expense data from a file
def load_data():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return {"expenses": []}

# Function to save expense data to a file
def save_data(data):
    with open("expenses.json", "w") as file:
        json.dump(data, file)

# Function to add an expense
def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense = {"amount": amount, "category": category, "description": description, "date": date}
    data["expenses"].append(expense)
    print("Expense added successfully!")

# Function to list all expenses
def list_expenses(data):
    if data["expenses"]:
        print("List of expenses:")
        for expense in data["expenses"]:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
    else:
        print("No expenses recorded.")

# Function to calculate total expenses for a specified time frame
def calculate_total_expenses(data, start_date, end_date):
    total_expenses = 0
    for expense in data["expenses"]:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S")
        if start_date <= expense_date <= end_date:
            total_expenses += expense["amount"]
    return total_expenses

# Function to generate monthly report
def generate_monthly_report(data, month, year):
    monthly_expenses = {}
    for expense in data["expenses"]:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d %H:%M:%S")
        if expense_date.month == month and expense_date.year == year:
            category = expense["category"]
            if category not in monthly_expenses:
                monthly_expenses[category] = expense["amount"]
            else:
                monthly_expenses[category] += expense["amount"]
    print(f"Monthly report for {month}/{year}:")
    for category, amount in monthly_expenses.items():
        print(f"{category}: {amount}")

# Main function
def main():
    data = load_data()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(data)
            save_data(data)
        elif choice == "2":
            list_expenses(data)
        elif choice == "3":
            start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
            end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
            total_expenses = calculate_total_expenses(data, start_date, end_date)
            print(f"Total expenses from {start_date.date()} to {end_date.date()}: {total_expenses}")
        elif choice == "4":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            generate_monthly_report(data, month, year)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
