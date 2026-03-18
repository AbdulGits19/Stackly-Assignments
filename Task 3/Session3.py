# Section 1: Loop Basics (1–10)

for i in range(1,51):
    print(i)

for i in range(1,101):
    if i % 2 == 0:
        print(i)

for i in range(1,101):
    if i % 2 != 0:
        print(i)

for i in range(1,11):
    print(f' 7 x {i} = {7*i}')

sum = 0
for i in range(1,101):
    sum += i

print(sum)

for i in range(50,0,-1):
    print(i)

div_by_3 = 0
for i in range(1,101):
    if i % 3 == 0:
        div_by_3 += 1
        
print(div_by_3)

for i in range(1,11):
    print(i*i)

for i in range(1,11):
    print(i**3)


input_user = int(input())
for i in range(input_user + 1):
    print(i)


# Section 2: While Loop (11–15)

start = 0
while start <= 20:
    print(start)
    start += 1

inp = int(input())
fact = 1
i = 1
while i <= inp:
    fact *= i
    i += 1

print(fact)

num = 1234
rev = 0

while num:
    
    unit = num % 10
    
    rev = unit + rev * 10
    
    num = num // 10
    
print(rev)

n = 896
dig_count = 0
while n:
    dig_count+= 1
    n = n // 10
    
print(dig_count)   
    
while True:
    inp = input('Enter something: ')
    if inp == 'stop':
        break
print("User entered 'stop', loop exited")

# Section 3: Nested Loop (16–20)
                        
for i in range(1,5):
    for j in range(i):
        print(j+1, end = '')
    print()

for i in range(1,6):
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
        if j == 10:
            print()

loop = 3
curr = 1
for i in range(loop):
    for j in range(loop):
        print(curr, end = ' ')
        curr += 1
    print()

# Section 4: String Basics (21–25)

count = 0
strn = 'stackly'
for i in strn:
    count += 1

print(count)

vow = 0

strn = 'stackly it company'

for i in strn:
    if i in 'aeiou':
        vow += 1
        
print(vow)

cons = 0

strn = 'stackly it company'

for i in strn:
    if i != ' ' and i not in 'aeiou':
        cons += 1
        
print(cons)

strn = 'stackly'
rev = ''

for i in strn:
    rev = i + rev
    
print(rev)

strn = 'stackly'
rev = ''

for i in strn:
    rev = i + rev
    
print(f'Is {rev} a palindrome : {rev == strn}')

# Section 5: String Slicing (26–30)

strn = 'stackly'
print(strn[:5])

strn = 'stackly'
print(strn[-3:])

strn = 'stackly'
print(strn[::-1])

strn = 'stackly'
print(strn[::2])

strn = 'stackly'
print(strn[1:-1])

# Section 6: List Basics (31–35)
                        
nums = [10,20,30,40,50]
total = sum(nums)
print(total)

numbers = [10,20,30,40,50]
max_num = max(numbers)
print(max_num)

numbers = [10,20,30,40,50]
min_num = min(numbers)
print(min_num)

numbers = [10,20,30,40,50]
count = len(numbers)
print(count)

numbers = [10,20,30,40,50]
print(50 in numbers)
print(120 in numbers)

# Section 7: List Operations (36–40)
                            
numbers = [10,20,30,40,50]
numbers.append(60)
numbers.append(70)
numbers.append(80)

print(numbers)

numbers = [10,20,30,40,50]
numbers.insert(2,25)
print(numbers)

lst = ['a','b','c','d']
lst.remove('a')
print(lst)

lst = ['a','b','c','d']
rev = []
for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])
print(rev)

lst = [1,4,3,9,2,7,5,6,8]

#bubble sort implementation

for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            
print(lst)