import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod

# Database Connection with database task8

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SSabMySQL@7860",
    database="task8"
)

cursor = conn.cursor()
print(' SQL Connection Successful!!! ')

# ABSTRACT CLASS creation

class BaseABC(ABC):

    @abstractmethod
    def show_details(self):
        pass


# USER CLASS definition

class User(BaseABC):

    def __init__(self, name):
        self.__name = name  

        # encapsulation by '__.name' 
        # hiding data is happening here

    def add_user(self):
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (self.__name,))
        conn.commit()
        print(f"User got added successfully!")

    def show_details(self):
        print(f"User: {self.__name}")


# EXPENSE CLASS definition 

class Expense(User):   # inheritance starts by inheriting User class 

    def __init__(self, name, amount, category, description, date):
        super().__init__(name)  
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    # method overriding
    def show_details(self):
        print(f"{self.category} : {self.amount} on {self.date}")

    def add_expense(self, user_id):
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (user_id, self.amount, self.category, self.description, self.date)

        cursor.execute(query, values)
        conn.commit()
        print("Expense added!")

    @staticmethod
    def get_all_expenses(user_id):
        query = """
        SELECT u.name, e.exp_id, e.amount, e.category, e.description, e.date
        FROM expenses e
        JOIN users u ON e.user_id = u.user_id
        WHERE u.user_id = %s
        """
        cursor.execute(query, (user_id,))
        return cursor.fetchall()


# Function Definitions 

# View expenses
def view_expenses():
    user_id = int(input("Enter user ID: ")) #1
    data = Expense.get_all_expenses(user_id)

    for i in data:
        print(i)


# Filter expenses 
def filter_expenses():
    user_id = int(input("Enter user ID: "))
    data = Expense.get_all_expenses(user_id)

    choice = input("Filter by (category/date): ")


    if choice == "category":
        cat = input("Enter category: ")
        result = list(filter(lambda x: x[3] == cat, data))
    
    
    # This is similar to the below sql command
    # SELECT * FROM table_name where category = 'any_category';
    

    elif choice == "date":
        dt = input("Enter date (YYYY-MM-DD): ")
        result = list(filter(lambda x: str(x[5]) == dt, data))

    
    # This is similar to the below sql command
    # SELECT * FROM table_name where date = 'any_date';
    

    else:
        print("Invalid choice")
        return

    print("\nFiltered Results:")
    for r in result:
        print(r)


# Total expense using map and reduce
def total_expense():
    user_id = int(input("Enter user ID: "))
    data = Expense.get_all_expenses(user_id)

    amounts = list(map(lambda x: x[2], data))

    if amounts:
        total = reduce(lambda a, b: a + b, amounts)
        print("Total Expense:", total)
    else:
        print("No such data exists ")


# Category-wise spending
def category_wise():
    user_id = int(input("Enter user ID: "))
    data = Expense.get_all_expenses(user_id)

    categories = set(map(lambda x: x[3], data))

    result = {
        cat: sum(x[2] for x in data if x[3] == cat)
        for cat in categories
    }

    print("\n Category-wise Spending:")
    for k, v in result.items():
        print(f"{k}: {v}")


# Delete expense
def delete_expense():
    exp_id = int(input("Enter expense ID to delete: "))
    cursor.execute("DELETE FROM expenses WHERE exp_id = %s", (exp_id,))
    conn.commit()
    print("Deleted successfully!")


# Update expense
def update_expense():
    exp_id = int(input("Enter expense ID: "))
    new_amount = float(input("Enter new amount: "))

    cursor.execute(
        "UPDATE expenses SET amount = %s WHERE exp_id = %s",
        (new_amount, exp_id)
    )
    conn.commit()
    print("Updated successfully!")


# Monthly report
def monthly_report():
    user_id = int(input("Enter user ID: "))

    query = """
    SELECT MONTH(date), SUM(amount)
    FROM expenses
    WHERE user_id = %s
    GROUP BY MONTH(date)
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    print("\nMonthly Report:")
    for row in data:
        print(f"Month {row[0]}: {row[1]}")


# Highest expense using reduce
def highest_expense():
    user_id = int(input("Enter user ID: "))
    data = Expense.get_all_expenses(user_id)

    if not data:
        print("No such expenses exist")
        return

    highest = reduce(lambda a, b: a if a[2] > b[2] else b, data)

    print("Highest Expense:", highest)


# Smart insight
def smart_insight():
    user_id = int(input("Enter user ID: "))
    data = Expense.get_all_expenses(user_id)

    if not data:
        print("No such data exists")
        return

    categories = {}
    for row in data:
        categories[row[3]] = categories.get(row[3], 0) + row[2]

    max_cat = max(categories, key=categories.get)

    print(f"You are spending too much on {max_cat}")


# Menu Driven Functoinality

def execute():

    while True:
        print("\n==== Smart Expense Manager ====")
        print("1. Add User")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Filter Expenses")
        print("5. Total Expense")
        print("6. Category-wise Spending")
        print("7. Delete Expense")
        print("8. Update Expense")
        print("9. Monthly Report")
        print("10. Highest Expense")
        print("11. Smart Insight")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            user = User(name)
            user.add_user()

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            name = input("Enter name: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")

            exp = Expense(name, amount, category, desc, date)
            exp.add_expense(user_id)

        elif choice == "3":
            view_expenses()

        elif choice == "4":
            filter_expenses()

        elif choice == "5":
            total_expense()

        elif choice == "6":
            category_wise()

        elif choice == "7":
            delete_expense()

        elif choice == "8":
            update_expense()

        elif choice == "9":
            monthly_report()

        elif choice == "10":
            highest_expense()

        elif choice == "11":
            smart_insight()

        elif choice == "12":
            print("Program is terminated!")
            break

        else:
            print("Invalid choice")


execute()