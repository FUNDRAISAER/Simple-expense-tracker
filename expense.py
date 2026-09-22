import json

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
print(expenses)

def save_expenses(expenses):
        with open("expense.json", 'w', encoding='utf-8') as file:
            json.dump(expenses, file)
        
def add_expense():
    categories = [
    "Food",
    "Transport",
    "Bills",
    "Shopping",
    "Entertainment",
    "Other"
    ]

    for key, value in enumerate(categories, start=1):
        print(f"{key}: {value}")

    try: 
        choice = int(input("Enter a category: "))
        if 1 <= choice <= len(categories):
            selected_category = categories[choice - 1]
            print("")
        else:
            print(f"\nInvalid choice. Please pick a number between 1 and {len(categories)}.")

    except ValueError:
        print("\nError: Please enter a valid number, not text.")

add_expense()
