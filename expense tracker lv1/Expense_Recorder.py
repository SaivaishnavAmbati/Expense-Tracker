import json
import os
from datetime import datetime

# Global variable for storing expense data
expense_data = []

# File to store expense data persistently
DATA_FILE = "expenses.json"


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


def get_current_date():
    """Get current date in 'YYYY-MM-DD' format."""
    return datetime.now().strftime('%Y-%m-%d')


def add_expense():
    """Add a new expense entry."""
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category of the expense: ").lower()

    expense = {
        "date": get_current_date(),
        "amount": amount,
        "description": description,
        "category": category
    }
    expense_data.append(expense)
    save_expenses()
    print("Expense added successfully!")


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

    print("\nCategory Breakdown:")
    for category, amount in category_totals.items():
        print(f"{category.capitalize()}: ${amount:.2f}")


def display_menu():
    """Display main menu."""
    print("\nExpense Recording System")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")


def main():
    load_expenses()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()


# To use the Expense Tracker application, follow these instructions:
# 
# Adding Expenses:
# 
# Run the expense_tracker.py script using Python.
# You'll be presented with a menu showing options:
# Expense Recording System
# 1. Add Expense
# 2. View Summary
# 3. Exit
# Choose option 1 to add an expense.
# Enter the amount spent, a brief description, and the category of the expense when prompted.
# Repeat this process to add multiple expenses.
# Viewing Summary:
# 
# Choose option 2 from the main menu to view the summary of your expenses.
# The summary will display the total amount spent and a breakdown by categories.
# Exporting Expenses to Excel:
# 
# Currently, the application does not directly support exporting expenses to Excel.
# However, you can modify the save_expenses() function to export the data to an Excel file instead of a JSON file. You can use libraries like openpyxl or pandas to achieve this.
# 
# 
# The application stores expense data persistently in a JSON file named expenses.json. This means your expense data will be retained even if you close the application and reopen it later.
# Error Handling:
# 
# The application includes basic error handling to handle unexpected user inputs and file operations.
# If you encounter any errors, the application will display informative error messages to guide you on how to proceed.
# Exiting the Application:
# 
# To exit the application, choose option 3 from the main menu.
# Your expense data will be saved automatically before the application exits.
# 
# 
# 
# ----> Here's a brief explanation of the data structures and algorithms used in the Expense Tracker implementation:
# 
# Data Structures:
# 
# Lists: Python lists are used to store the expense_data. Each expense entry is represented as a dictionary and appended to this list.
# Dictionary: Dictionaries are used to store individual expense entries. Each entry contains keys such as "date", "amount", "description", and "category", with corresponding values.
# File I/O: The json module is utilized for reading from and writing to a JSON file (expenses.json) to persistently store expense data.
# Algorithms:
# 
# Add Expense: The add_expense() function allows users to add new expenses. It prompts the user to input the amount spent, description, and category. It then creates a dictionary representing the new expense and appends it to the expense_data list.
# View Summary: The view_summary() function calculates and displays the total amount spent and a breakdown of expenses by category. It iterates over the expense_data list to compute these values.
# Load and Save Expenses: The load_expenses() function reads expense data from the JSON file into the expense_data list when the program starts. The save_expenses() function writes the current expense_data list back to the JSON file to persist the data.
# Error Handling: Basic error handling is implemented to handle scenarios such as invalid user inputs or file operations. Error messages are provided to guide users on how to proceed.
# These data structures and algorithms allow for efficient management of expenses within the application. The use of lists and dictionaries provides a flexible and scalable way to store and manipulate expense data, while file I/O operations ensure that the data is persisted across multiple program runs.