import json
from datetime import datetime

def load_expenses():
    try:
        with open("expense.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data 
    except FileNotFoundError:
        print("Error: The file expense.json does not exist.")

        return []
    except json.JSONDecodeError:
        print("Error: The file exists. but it's not a valid JSON file.")
        return []

expenses = load_expenses()

def show_menu():
    menu = [
        "Add Expense",
        "View Expenses",
        "View Total",
        "Edit Expense",
        "Exit"
    ]

    while True:
        print("========== EXPENSE TRACKER ==========")

        for key, value in enumerate(menu, start=1):
            print(f"{key}. {value}")

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                new_expense = add_expense(expenses)
                expenses.append(new_expense)
                save_expenses(expenses)

            elif user_choice == 2:
                view_expenses(expenses)

            elif user_choice == 3:
                total = calculate_total(expenses)
                print(f"Total Expense: ${total}")

            elif user_choice == 4:
                edit_expense(expenses)

            elif user_choice == 5:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")


def save_expenses(expenses):
        with open("expense.json", 'w', encoding='utf-8') as file:
            json.dump(expenses, file, indent=2)

def select_category():
    categories = [
        "Food",
        "Transport",
        "Bills",
        "Shopping",
        "Entertainment",
        "Other"
    ]

    while True:
        for key, value in enumerate(categories, start=1):
            print(f"{key}: {value}")

        try:
            choice = int(input("Enter a category: "))

            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                print(f"You entered {selected_category}")
                return selected_category
            else:
                print(
                    f"\nInvalid choice. Please pick a number between 1 and {len(categories)}."
                )

        except ValueError:
            print("\nError: Please enter a valid number, not text.")

def get_amount():
    while True:
            try:
                amount = float(input("Enter an amount: $"))
                if amount > 0:
                    return amount
                else:
                    print("Not a valid amount. try again!")
            except ValueError:
                print("Amount not valid.")
                continue

def get_date():
    while True:
            try:
                date = input("Please enter a date (YYYY-MM-DD): ")  
                datetime.strptime(date, "%Y-%m-%d")
                return date
            except ValueError:
                print("Invalid date or format. Please try again.")            

def add_expense(expenses):
    selected_category = select_category()
    selected_description = input("Enter a description: ")
    amount = get_amount()
    date = get_date()

    existing_ids = []

    new_id = 1

    for expense in expenses:
        existing_ids.append(expense["ID"])

    while new_id in existing_ids:
         new_id += 1

    new_expense = {
    "ID": new_id,
    "Category": selected_category,
    "Description": selected_description,
    "Amount": amount,
    "Date": date
}
    return new_expense

def view_expenses(expenses):
    print("========== EXPENSES ==========")
    if not expenses:
            print("No expenses found. Your expense log is currently empty.")
    else:
        for item in expenses:
            print()
            print(
                f" ID: {item.get('ID')}.\n Category: {item.get('Category')}\n Description: {item.get('Description')}\n Amount: ${item.get('Amount')}\n"
                f" Date: {item.get('Date')}\n"
            )
            print("------------------------------")

def calculate_total(expenses):
    total = 0

    for item in expenses:
        total += item.get('Amount', 0)

    return total

def edit_expense(expenses):
    try:
        expense_id = int(input("Enter expense ID to edit: "))
    except ValueError:
        print("Not a valid ID number.")
        return

    found = False

    for expense in expenses:
        if expense["ID"] == expense_id:
            found = True

            selected_category = select_category()
            new_description = input("Enter new description: ")
            amount = get_amount()
            date = get_date()

            expense["Category"] = selected_category
            expense["Description"] = new_description
            expense["Amount"] = amount
            expense["Date"] = date

            save_expenses(expenses)
            print(expense)
            break

    if not found:
        print("Expense not found.")

show_menu()