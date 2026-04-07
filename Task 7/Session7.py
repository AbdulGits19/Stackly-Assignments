# 👉 Task 1: se super() properly 

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name,id)
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name,id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

user = User("Alekhya Maaran", 1)
student = Student("Jaan Begum", 2, "CSE", 50000)
faculty = Faculty("Dr. Goutham Srinivasan", 3, 100000)
temp_faculty = TempFaculty("Bob Marley", 4, 80000, "6 months")


user2 = User("Abdul", 1)
student2 = Student("Uday Karnan", 2, "CSE", 50000)
faculty2 = Faculty("Dr. Samson", 3, 100000)
temp_faculty2 = TempFaculty("John Durairaj", 4, 80000, "6 months")

# The code, if runs without errors, it proves super() works perfectly!!!!
print("\n-------------- Inheritance Working -----------------------")
print(f"\nUser: Name = '{user.name}', ID = {user.id}")
print(f"\nStudent: Name = '{student.name}', ID = {student.id}, Dept = '{student.dept}', Fees = {student.fees}")
print(f"\nFaculty: Name = '{faculty.name}', ID = {faculty.id}, Salary = {faculty.salary}")
print(f"\nTempFaculty: Name = '{temp_faculty.name}', ID = {temp_faculty.id}, Salary = {temp_faculty.salary}, Duration = '{temp_faculty.duration}'")
print('\n--------------------------------------------------------------')
print(f"\nUser: Name = '{user2.name}', ID = {user2.id}")
print(f"\nStudent: Name = '{student2.name}', ID = {student2.id}, Dept = '{student2.dept}', Fees = {student2.fees}")
print(f"\nFaculty: Name = '{faculty2.name}', ID = {faculty2.id}, Salary = {faculty2.salary}")
print(f"\nTempFaculty: Name = '{temp_faculty2.name}', ID = {temp_faculty2.id}, Salary = {temp_faculty2.salary}, Duration = '{temp_faculty2.duration}'")


# 👉 Task 2: Apply Abstraction 


from abc import ABC, abstractmethod

# Here, i have defined a 'Base Class'
class AbstractUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    @abstractmethod
    def get_details(self):
        pass


class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
    
    def get_details(self):
        return f"Student: {self.name} (ID: {self.id}), Dept: {self.dept}, Fees: ₹{self.fees}"

class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    
    def get_details(self):
        return f"Faculty: {self.name} (ID: {self.id}), Salary: ₹{self.salary:,}"

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
    
    def get_details(self):
        return f"Temp Faculty: {self.name} (ID: {self.id}), Salary: ₹{self.salary:,}, Duration: {self.duration}"
        
# If these implementations run properly, then 'Abrstract Class' is handled right!!

student = Student("Thanish Deep", 2, "CSE", 50000)
faculty = Faculty("Sarah Cooper", 3, 100000)
temp_faculty = TempFaculty(" Ian Mckellen", 4, 90000, "6 months")

print(student.get_details())
print(faculty.get_details())
print(temp_faculty.get_details())


# 👉 Task 3: Sorting using key


students = [student, student2]
faculty_list = [faculty, faculty2]


sorted_students = sorted(students, key=lambda x: x.fees)
sorted_faculty = sorted(faculty_list, key=lambda x: x.salary)


print("\n------ Sorted Students by fees ------")
for s in sorted_students:
    print(s.name, s.fees)

print("\n------ Sorted Faculty by salary ------")
for f in sorted_faculty:
    print(f.name, f.salary)


# 👉 Task 4: Use map()


students = [student, student2]
print("\n------ Student Names ------")
print()
print(list(map(lambda s: s.name, students)))


# 👉  Task 5: Use filter()


high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
high_salary_faculty = list(filter(lambda f: int(f.salary) > 30000, faculty_list))


print("\n------ Students with Fees > 50000 ------")
for s in high_fee_students:
    print(s.name, s.fees)

print("\n------ Faculty with Salary > 30000 ------")
for f in high_salary_faculty:
    print(f.name, f.salary)


# 👉 Task 6: Use reduce()


from functools import reduce


total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
total_salary = reduce(lambda acc, f: acc + int(f.salary), faculty_list, 0)


print("\n------ Total Fees Collected ------")
print(total_fees)
print("\n------ Total Salary of Faculty ------")
print(total_salary)


# 👉 Task 7: Higher Order Function

# Higher Order Function
def process_users(users, func):
    return list(map(func, users))


names = process_users(students, lambda s: s.name)
print("\n------ Names using HOF ------")
print(names)

fees = process_users(students, lambda s: s.fees)
print("\n------ Fees using HOF ------")
print(fees)

