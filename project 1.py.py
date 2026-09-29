# Expense tracker 1

import json
import os

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")

expenses = []


def load_expenses():
    global expenses
    try:
        with open(FILE_PATH, "r") as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []

def save_expenses():
    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)

load_expenses() 

while True:
    print("====menu====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Search Expenses")
    print("5. Delete Expenses")
    print("6. Edit Expenses")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

# add expense
    if choice == 1:
        print("==== Add Expense ====")
        date = input("Enter the date (dd/mm/yyyy): ")
        category = input("Enter the category of expense (food, transport, entertainment): ")  
        description = input("Enter the description of expense: ")
        amount = float(input("Enter the amount of expense: "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        save_expenses()
        print ("done bro! Expense added successfully!")
        
# view the expenses
    elif choice == 2:
            print("==== view your expenses ====")
            if (len(expenses) == 0):
                print("No expenses  are added")
            else:
                print("==== your total expenses ====")
                count = 1
                for eachexpense in expenses:
                    print(f"expense number {count}->  {eachexpense['date']},  {eachexpense['category']},  {eachexpense['description']}, {eachexpense['amount']}") 
                    count = count + 1

# view total expenses
    elif choice == 3:
        print("==== view total expenses ====")
        total = 0
        for expense in expenses:
            total = total + expense['amount']
        print("\nTotal Expenses = ", total)

# search expenses
    elif choice == 4:
        if len(expenses)==0:
            print("no expenses are added")
        else:
            searchdate = input("enter date: ")
            searchcategory = input("enter category: ")

            found = False
            for expense in expenses:
                if expense["date"] == searchdate and expense["category"].lower() == searchcategory.lower():

                    print("expenses found!")
                    print("date:",expense["date"])
                    print("category:",expense["category"])
                    print("description:",expense["description"])
                    print("amount:",expense["amount"])

                    found = True


            if not found:
                print("no expenses found.")

# delete expenses
    elif choice == 5:
        if len(expenses)==0:
                print("no expenses are added")                

        else:
            print("==== your total expenses ====")
            count = 1
            for eachexpense in expenses:
                print(f"expense number {count}->  {eachexpense['date']},  {eachexpense['category']},  {eachexpense['description']}, {eachexpense['amount']}") 
                count = count + 1

            delete_number = int(input("Enter the expenses number you want to  delete: "))
            if delete_number >=1 and delete_number<= len(expenses):
                expenses.pop(delete_number - 1)
                save_expenses()
                print("expense deleted successfully")

            else:
                print("invalid expense number.")

# edit expenses
    elif choice == 6:
            if len(expenses)==0:
                print("no expenses are added")                
    
            else:
                print("==== your total expenses ====")
                count = 1
                for eachexpense in expenses:
                    print(f"expense number {count}->  {eachexpense['date']},  {eachexpense['category']},  {eachexpense['description']}, {eachexpense['amount']}") 
                    count = count + 1

                edit_number = int(input("enter the expenses number you want to edit:"))
                if edit_number >=1 and edit_number <= len(expenses):
                    expense = expenses[edit_number - 1]

                    print("\nenter new details:")
                    expense["date"] = input("Enter the date (dd/mm/yyyy): ")
                    expense["category"] = input("Enter the category of expense (food, transport, entertainment): ")  
                    expense["description"] = input("Enter the description of expense: ")
                    expense["amount"] = float(input("Enter the amount of expense: "))
                    save_expenses()
                    print("expense updated successfully")

                else:
                     print("invalid expense number")


# exit the program
    elif choice == 7:
        save_expenses()
        print("thank you for using the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")