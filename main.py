import csv

def add_expense():
    amount = float(input("Enter amount spent: "))
    description = input("Enter brief description: ")
    category = input("Enter category: ")
    # store data in dictionary
    expense = {'amount': amount, 'description': description, 'category': category}
    # write data to file
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense.values())
    print("Expense added successfully!")

def view_expenses():
    # read data from file
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def monthly_expenses():
    # calculate total expenses for the month
    # read data from file and filter by month
    pass

def category_expenses():
    # calculate total expenses for each category
    # read data from file and group by category
    pass

while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Expenses")
    print("4. Category-wise Expenses")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        monthly_expenses()
    elif choice == '4':
        category_expenses()
    elif choice == '5':
        break
    else:
        print("Invalid option!")