# --------------- Mini Project 1: Employee Management System ---------------

employees = []


def add_employee(name, age, role, salary):
    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }
    employees.append(emp)


def display_employees():
    for employee in employees:
        print(employee)


def update_employee(name, new_data):
    for emp in employees:
        if emp["name"] == name:
            emp.update(new_data)
            return "New Data Updated successfully!!"
    return "Employee not found"


def delete_employee(name):
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            return "Employee, Deleted successfully!!"
    return "Employee not found"



add_employee("Abdul", 22, "Developer", 50000)
add_employee("Divya", 25, "UI Designer", 40000)

print('Before: ', end = ' ')
display_employees()
print()

update_employee("Abdul", {"salary": 60000})

delete_employee("Divya")

print('After: ', end = ' ')
display_employees()


# ---------------- Mini Project 2: Student Report Card ----------------

def report(name, m, p, c): # m - maths # p - physics # c- chemistry
    
    marks = {
        "name": name,
        "m": m,
        "p": p,
        "c": c
    }

    total = marks["m"] + marks["p"] + marks["c"]
    avg = total / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    print("\n" + "="*45)
    print(" "*12 + "STUDENT REPORT CARD")
    print("="*45)
    print(f"Name       : {marks['name']}")
    print(f"Maths      : {marks['m']}")
    print(f"Physics    : {marks['p']}")
    print(f"Chemistry  : {marks['c']}")
    print("-"*45)
    print(f"Total      : {total}")
    print(f"Average    : {avg:.2f}")
    print(f"Grade      : {grade}")
    print("="*45)


# usage
report("Abdul", 69, 77, 88)
report("Charan", 90, 68, 77)

# --------------- Mini Project 3: Shopping Cart System ---------------

products_db = {
    
    # Electronics
    "Laptop"                    : 45000,
    "Gaming Laptop"             : 95000,
    "Mouse"                     : 500,
    "Keyboard"                  : 2500,
    "Headphones"                : 1800,
    "Gaming Headset"            : 4500,
    "Mobile Phone"              : 18000,
    "Smart Watch"               : 8000,
    "USB Cable"                 : 150,
    "Power Bank"                : 1200,
    "Laptop Bag"                : 900,

    # StationERY
    "Pen"                       : 20,
    "Refill Pen"                : 35,
    "Notebook"                  : 80,
    "Sketch Book"               : 150,
    "Pencil"                    : 10,
    "Eraser"                    : 5,
    "Sharpener"                 : 15,
    "Ruler 30cm"                : 25,
    "Geometry Box"              : 120,
    "Highlighter Set"           : 80,

    # Snacks & Drinks
    "Chips Pack"                : 20,
    "Chocolates"                : 50,
    "Biscuits Packet"           : 30,
    "Cold Drink 1L"             : 45,
    "Energy Drink"              : 70,
    "Peanuts 200g"              : 90,

    # Clothes & Accessories
    "T‑Shirt Cotton"            : 399,
    "Jeans"                     : 1299,
    "Hoodie"                    : 799,
    "Casual Shoes"              : 1499,
    "Socks 3 Pairs"             : 199,
    "Cap"                       : 250,
    "Wallet"                    : 450,

    # Home & Personal
    "Wall Clock"                : 750,
    "LED Bulb 9W"               : 85,
    "Toothbrush"                : 50,
    "Toothpaste 100g"           : 120,
    "Face Wash 100ml"           : 180,
    "Sanitizer Mini "           : 60
}

cart = []


def show_available():
    
    print("\nAvailable Products:")
    print("-" * 30)
    for name, price in products_db.items():
        print(f"{name:<15}       ₹{price}")



def add_to_cart(name, quantity):
    if name not in products_db:
        print(f"'{name}' is not available. Please choose from the list.\n")
        return

    price = products_db[name]
    
    for item in cart:
        if item["name"] == name:
            item["quantity"] += quantity
            print(f"Updated '{name}' quantity in cart.\n")
            return

    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })
    print(f"'{name}' (x{quantity}) added to cart.\n")


def remove_from_cart(name):
    
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            print(f"'{name}' removed from cart.\n")
            return
    print(f"'{name}' not found in cart.\n")


def calculate_total():
    
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


def show_cart():
    """Display all items in cart in a formatted way."""
    print("\n" + "="*50)
    print("                  SHOPPING CART")
    print("="*50)

    if not cart:
        print("Your cart is empty.")
    else:
        for item in cart:
            line_total = item["price"] * item["quantity"]
            print(f"{item['name']:<15} ₹{item['price']:<8} × {item['quantity']:<2} = ₹{line_total}")

    total = calculate_total()
    print("-"*50)
    print(f"TOTAL BILL: ₹{total}")
    print("="*50)



show_available()

add_to_cart("Laptop", 1)
add_to_cart("Mouse", 2)
add_to_cart("Headphones", 1)
add_to_cart("Oven", 1)      #error because no such product in db
show_cart()

remove_from_cart("Mouse")

show_cart()

# --------------- Mini Project 4: Login & User Validation ---------------

def login_portal():
    
    print('-- Welcome to login portal --\n')
    
    users_db = {
        'Abdul_Basith_19': 'abdulbasith@1953',
        'Janani_Madhavi': 'janmad1932',
        'Ali_Yasmin99': 'aliyasmin@2024',
        'Rani_Kumari': 'ranidata120@130',
        'Tara_Singh_27': 'tarasingh100@99',
        'David99': 'davidisreal123'
    }
    
    
    username = input('Enter username: ').strip()
    password = input('Enter password: ').strip()
    
    print()
    print()
    
  
    if username in users_db:
        
        if users_db[username] == password:
            print('Login Successful! Welcome,', username.capitalize())
        else:
            print('Wrong password! Try again.')
            
    else:
        print(f'Uh,Oh! Username "{username}" does not exist. Please register first.')



login_portal()

# --------------- Mini Project 5: Unique Visitor Counter ----------------

visited = set()

def add_visitor(name):
    
    if name not in visited:
        visited.add(name)
        print(name, 'added')
        
def display_count():
    
    print(len(visited))
    
    
add_visitor('Abdul')
add_visitor('Abdul')  # duplicate
add_visitor('Madhu')

print("Current visitors:", visited)
display_count()

# ---------------- Mini Project 6: String Formatter Tool ----------------

def formatter(name, product):
    
    sentence = f"{name} purchased a {product}."
    
    print("\n--- Formatted Output ---\n")
    
    print("Sentence:")
    print(sentence)
    
    print("\nLeft aligned:")
    print(f"{sentence:<40}")
    
    print("\nRight aligned:")
    print(f"{sentence:>40}")
    
    print("\nCenter aligned:")
    print(f"{sentence:^40}")
    
formatter('Abdul', 'PS5')


# --------------- Mini Project 7: Bank Account System ---------------

account = dict()


def create_account(name, initial_balance=0):
    account["name"] = name
    account["balance"] = initial_balance
    print(f"Account created for {name} with balance ₹{initial_balance}.")


def deposit(amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
        return

    account["balance"] += amount
    print(f"₹{amount} deposited. New balance: ₹{account['balance']:.2f}")


def withdraw(amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return

    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount
    print(f"₹{amount} withdrawn. New balance: ₹{account['balance']:.2f}")


def check_balance():
    print(f"Balance for {account['name']}: ₹{account['balance']:.2f}")


create_account("Abdul Basith", 5000)

deposit(2000)
withdraw(1500)
check_balance()

withdraw(6000)  # "Insufficient balance"

#  --------------- Mini Project 8: Voting System ---------------

voters_db = { 'Ramesh' : 7, 'Suresh' : 9, 'Dinesh' : 4}

def add_vote(name):
    if name in voters_db.keys():
        voters_db[name] += 1
        print(f'Vote added for {name}')
    else:
        print('No such voter exists!')
        
def election_winner():
    
    max_votes = 0
    winner = None
    
    for i,j in voters_db.items():
        if j > max_votes:
            max_votes = j
            winner = i
            
    print(f"Winner of the elections : {winner}")
    
add_vote('Ramesh')
add_vote('Suresh')
add_vote('Suresh')
add_vote('Suresh')
election_winner()

#  Mini Project 9: Course Enrollment System

enrollments = {}

def add_student(name, courses):
    
    if name in enrollments:
        print(f"Error: {name} is already enrolled. Use update instead.")
    else:
        enrollments[name] = list(courses)
        print(f"Added {name} with {len(courses)} courses.")

def update_courses(name, new_courses):
    if name in enrollments:
        enrollments[name].extend(new_courses)
        enrollments[name] = list(set(enrollments[name]))
        print(f"Updated courses for {name}.")
    else:
        print(f"Error: Student '{name}' not found.")

def display_details(name):
    if name in enrollments:
        print(f"\n--- Student Profile ---")
        print(f"Name:    {name}")
        print(f"Courses: {', '.join(enrollments[name])}")
    else:
        print(f"Error: Student '{name}' not found.")

# --- Testing the System ---
add_student("Alice", ["Biology", "Chemistry"])
add_student("Bob", ["Calculus"])

update_courses("Alice", ["Physics", "History"])

display_details("Alice")
display_details("Bob")

# --------------- Mini Project 10: Number Utility Tool ---------------

def convert_bases(num):

    print(f"\nBase conversions for {num}:")
    print(f"Binary  : {num:b}")
    print(f"Octal   : {num:o}")
    print(f"Hex     : {num:X}")


def format_with_commas(num):
    formatted = f"{num:,}"
    print(f"Formatted with commas: {formatted}")


def to_scientific_notation(num):
    sci = f"{num:e}"
    print(f"Scientific notation  : {sci}")


def show_number_info(num):
    """Show all utilities for a number."""
    print("=" * 50)
    print("           NUMBER UTILITY TOOL")
    print("=" * 50)
    print(f"Number (Integer Representation) : {num}")

    convert_bases(num)
    format_with_commas(num)
    to_scientific_notation(num)


show_number_info(1234567)
show_number_info(255)
show_number_info(999999999)