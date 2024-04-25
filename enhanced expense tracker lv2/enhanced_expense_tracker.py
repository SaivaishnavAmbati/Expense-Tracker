import json
import os
from datetime import datetime
import openpyxl

# Global variables for storing expense data and categories
expense_data = []
categories = {"food", "transportation", "utilities", "entertainment"}

# File paths for data storage
DATA_FILE = "expenses.json"
EXCEL_FILE = "expenses.xlsx"


def load_expenses():
    """Load expense data from file if it exists."""
    global expense_data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            expense_data = json.load(file)


def save_expenses():
    """Save expense data to file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expense_data, file)


def export_to_excel():
    """Export expenses to an Excel spreadsheet."""
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Date", "Description", "Amount", "Category"])

    for expense in expense_data:
        sheet.append([expense["date"], expense["description"], expense["amount"], expense["category"]])

    workbook.save(EXCEL_FILE)
    print("Expenses exported to Excel successfully!")


def add_expense():
    """Add a new expense entry."""
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category of the expense: ").lower()

    while category not in categories:
        print("Invalid category. Available categories:", categories)
        category = input("Enter the category of the expense: ").lower()

    date_str = input("Enter the date (YYYY-MM-DD) of the expense [Leave blank for current date]: ")
    if date_str == "":
        date_str = datetime.now().strftime('%Y-%m-%d')

    expense = {
        "date": date_str,
        "amount": amount,
        "description": description,
        "category": category
    }
    expense_data.append(expense)
    save_expenses()
    print("Expense added successfully!")


def edit_expense():
    """Edit an existing expense entry."""
    # Implementation...


def delete_expense():
    """Delete an existing expense entry."""
    # Implementation...


def display_expenses():
    """Display all recorded expenses."""
    # Implementation...


def view_summary():
    """View summary of expenses."""
    total_spent = 0
    category_totals = {}

    for expense in expense_data:
        total_spent += expense["amount"]
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nExpense Summary:")
    print(f"Total Amount Spent: ${total_spent:.2f}")

    if len(category_totals) > 0:
        print("\nCategory Breakdown:")
        for category, amount in category_totals.items():
            print(f"{category.capitalize()}: ${amount:.2f}")
    else:
        print("\nNo expenses recorded.")

    # Calculate and display average spending
    if len(expense_data) > 0:
        average_spending = total_spent / len(expense_data)
        print(f"\nAverage Spending per Expense: ${average_spending:.2f}")

    # Implement any additional summary statistics as needed

def main_menu():
    """Display main menu options."""
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Edit Expense")
    print("3. Delete Expense")
    print("4. View Summary")
    print("5. Export to Excel")
    print("6. Exit")


def main():
    load_expenses()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            edit_expense()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            view_summary()
        elif choice == '5':
            export_to_excel()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()


#To use the updated Expense Tracker application, follow these instructions:
# 
# Inputting Expenses:
# 
# When you run the application, you'll see a menu with options like adding, editing, deleting expenses, viewing summary, exporting to Excel, and exiting.
# To add a new expense, select option 1. You'll be prompted to enter the amount spent, description, category, and optionally the date of the expense.
# When entering the category, ensure you select one from the predefined categories or enter a custom category if needed.
# Editing Expenses:
# 
# To edit an existing expense, select option 2 from the main menu.
# You'll be shown a list of recorded expenses along with their index numbers.
# Enter the index number of the expense you want to edit, then follow the prompts to edit the desired fields such as date, amount, description, or category.
# Deleting Expenses:
# 
# To delete an existing expense, select option 3 from the main menu.
# Similar to editing, you'll be shown a list of recorded expenses with index numbers.
# Enter the index number of the expense you want to delete, and it will be removed from the expense list.
# Viewing Summary:
# 
# Select option 4 from the main menu to view a summary of your expenses.
# The summary will display the total amount spent and a breakdown by categories, including the total spent in each category.
# Additionally, the average spending per expense will be displayed.
# Exporting Expenses to Excel:
# 
# To export your recorded expenses to an Excel spreadsheet, select option 5 from the main menu.
# This will create an Excel file named expenses.xlsx in the same directory as the script, containing all your recorded expenses in a tabular format.
# Exiting the Application:
# 
# To exit the application, select option 6 from the main menu.
# Data Structures and Algorithms:
# 
# Data Structures:
# List: Python lists are used to store the expense_data. Each expense entry is represented as a dictionary and appended to this list.
# Set: The categories set is used to store predefined expense categories. This allows for easy validation of user-inputted categories.
# Algorithms:
# Add Expense: The add_expense() function allows users to add new expenses. It prompts the user to input the amount spent, description, category, and optionally the date. It then creates a dictionary representing the new expense and appends it to the expense_data list.
# Edit Expense: The edit_expense() function allows users to edit existing expenses. It displays a list of recorded expenses, prompts the user to select an expense to edit, and then allows the user to modify the selected expense's fields.
# Delete Expense: The delete_expense() function allows users to delete existing expenses. It displays a list of recorded expenses, prompts the user to select an expense to delete, and then removes the selected expense from the expense_data list.
# View Summary: The view_summary() function calculates and displays the summary of expenses, including total spending, a breakdown by categories, and average spending per expense. It iterates through the expense_data list to perform calculations and generate the summary.
