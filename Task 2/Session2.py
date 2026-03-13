# Bitwise Operator Tasks (1–8)

a,b =10,6
print(a & b)

x,y = 12,5
print(x | y)

num = 8
print(~num)

a,b = 15,9
print(a ^ b)

num = 7
print(num << 2)

num = 20
print(num >> 1)

x = int(input('Enter x: '))
y = int(input('Enter y: '))
print(f'AND Result : {x & y}')
print(f'XOR Result : {x ^ y}')

#-------------------------------------------------------------------

# String Tasks (9–14)

text = 'hi'
print((text + ' ') * 4)

strn = 'python'
print(strn,strn,strn)

s1 = 'super'
s2 = 'man'
print(s1 + s2)

str1 = 'hello'
str2 = ' '
str3 = 'world'
print(str1 + str2 + str3)

name = input('Enter your name: ') + ' '
print(name * 5)

str1 = input('Enter str1: ')
str2 = input('Enter str2: ')
print(str1 + ' ' + str2)

#-------------------------------------------------------------------

# Input & Type Casting Tasks (15–20)

name = input('Enter your name: ')
print(type(name))

age = input('Enter your age: ')
age = int(age)
print(age,type(age))

num1 = int(input('Enter num1: '))
num2= int(input('Enter num2: '))
print(f'Sum of num1 and num2 : {num1 + num2}')

mark1 = int(input('Enter first mark: '))
mark2 = int(input('Enter second mark: '))
print(f'Average : {(mark1 + mark2)/2}')

a = int(input('Enter num1: '))
b = int(input('Enter num2: '))
print(3*a*2 + b - 2)

num = input('Enter a number: ')
print('Before: ',type(num))
num = int(num)
print('After: ',type(num))

# -------------------------------------------------------------------

# Unit Digit Tasks (21–25)

number = input('Enter a num: ')
print(number[len(number) - 1])

number = int(input('Enter a num: '))
print(number % 10)

num = int(input('Enter a num: '))
print(num // 10)

number = input('Enter a num: ')
print(number[len(number) - 2])

five_num = 67893
print(five_num % 10)

#-------------------------------------------------------------------

# If Statement Tasks (26–30)

if 10 >= 5:
    print('Yes')
else:
    print('No')
    
num = int(input('Enter a number: '))
if num > 50:
    print(f'{num} is greater than 50')
elif num == 50:
    print(f'{num} is 50')
else:
    print(f'{num} is < 50')

age = int(input('Enter a num: '))
if age >= 18:
    print('Age is above 18')
else:
    print('Age is below 18')
    
number = 101
print(True if number >= 100 else False)

numer = 4
print(True if number >= 0 else False)

#-------------------------------------------------------------------

# If-Else Tasks (31–34)

num = 77
if num % 2 == 0:
    print('Even')
else:
    print('Odd')

user_marks = int(input('Enter your marks: '))
print('Pass' if user_marks >= 35 else 'Fail')

num = -6
print('Negative' if num < 0 else 'Positive')

number = 30
print('Greater than 10' if number > 10 else 'Less than 10')

#-------------------------------------------------------------------

# Nested If Tasks (35–37)

age = int(input("Enter Age: "))
height = int(input("Enter Height (cm): "))
weight = int(input("Enter Weight (kg): "))


if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected : All criterias satisfied")
        else:
            print("Rejected : Weight too low")
    else:
        print("Rejected : Height too low")
else:
    print("Rejected : Underage")


marks = int(input("Enter your Marks percentage: "))
age = int(input("Enter your Age: "))

if marks >= 60:
    
    if age >= 17:
        print("Congratulations! You are eligible for admission.")
    else:
        print("Rejected: You must be at least 17 years old.")
else:
    print("Rejected: Minimum 60% marks required.")


age = int(input("Enter Age: "))
height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))


if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Status: Selected for the Team!")
        else:
            print("Status: Rejected (Weight must be at least 50kg)")
    else:
        print("Status: Rejected (Height must be at least 150cm)")
else:
    print("Status: Rejected (Age must be at least 16)")

#-------------------------------------------------------------------

# Match Statement Tasks (38–40)

day_num = int(input("Enter day number from 1 to 7 : "))

match day_num:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid Day Number")

color_code = int(input('Select a Number from 1 to 3: '))

match color_code:
    case 1: print('Red')
    case 2: print('Blue')
    case 3: print('Green')
    case _: print("No color found")

fruit_id = int(input("Enter fruit id from 1 to 4 : "))

match fruit_id:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Fruit not found")



















