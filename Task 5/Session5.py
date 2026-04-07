# Task 1: User Info Manager (Functions + Dictionary)

all_users = []

def create_user(name, age, role):
    f_name = name.title()
    user = {'name': f_name, 'age': age, 'role': role}
    all_users.append(user)
    print(user)
    
def return_all_users():
    print()
    print('---------- Users -----------')
    for i in range(len(all_users)):  
        print(f' {i+1} - {all_users[i]["name"]}')
    print('-----------------------------')

create_user('Gaurav', 29, 'UI/UX Designer')
create_user('Abhinay', 27, 'Ruby Developer')
create_user('Yunus', 26, 'Linux Engineer')
return_all_users()



# Task 2: Dynamic Calculator (*args)

def calculate_total(*nums):
    sum_x = 0
    for num in nums:
        sum_x += num

    avg_nums = sum_x / len(nums)
    
    return f' Sum : {sum_x}, Avg : {avg_nums}'

print(calculate_total(1,2,3,4,5,6,7,8,9,10))



#  Task 3: Keyword Config System (**kwargs)

def system_config(**multis):
    print("All key-value pairs:")
    for key, value in multis.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")
system_config(mode="recover", version="2.6")



# Task 4: Factorial Service (Recursion)

def factorial(n):

    if n < 0: # This condition handles Negative Numbers
        return 'No Factorial Exists for Negative Numbers'
    
    if n == 0: # This condition handles 0
        return 1
    
    return n * factorial(n-1)

print(factorial(5))


# Task 5: Memory Optimization (Generator)


def square_list(n):
    return [i*i for i in range(n)]

def square_generator(n):
    for i in range(n):
        yield i*i

lst = square_list(5)
genr = square_generator(5)

print(lst)
print(next(genr))
print(next(genr))
print(next(genr))
print(next(genr))
print(next(genr))


print(type(lst))
print(type(genr))


# Task 6: Exception Handling Module

num = 10
den = 0

try:
    print(num/den)

except ZeroDivisionError:
    print('Invalid Input, Try removing zero from the denominator')
    
finally:
    print('Program Completed')


#  Task 7: File Handling

# 1. Create and Write 
user_details = "Name: Abdul, Role: Python Developer, Department: Software Development"

with open("team_data.txt", "w") as file:
    file.write(user_details)
    print("Data successfully written to team_data.txt")

# 2. Read and Display content
print("\nReading file content:")
with open("team_data.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Closing

if file.closed:
    print("\nThe file is confirmed CLOSED.")
else:
    print("\nThe file is still OPEN.")