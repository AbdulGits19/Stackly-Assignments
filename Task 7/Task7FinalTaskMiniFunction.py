from functools import reduce


class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, Fees: {self.fees}"


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"


# -------- Data --------
students = [
    Student("Ali", 50000),
    Student("Karan", 30000),
    Student("Sara", 70000)
]

faculty = [
    Faculty("Tarun Rao", 100000),
    Faculty("Kaanth", 70000),
    Faculty("Yugesh Darsh", 25000)
]


# -------- 1. Print All Details (map) --------
print("\n--- ALL DETAILS ---")

student_details = list(map(lambda s: s.get_details(), students))
faculty_details = list(map(lambda f: f.get_details(), faculty))

for d in student_details:
    print(d)

for d in faculty_details:
    print(d)


# -------- 2. Sorted Data --------
print("\n--- SORTED ---")

sorted_students = sorted(students, key=lambda s: s.fees)
sorted_faculty = sorted(faculty, key=lambda f: f.salary)

print("\nStudents (by fees):")
for s in sorted_students:
    print(s.name, s.fees)

print("\nFaculty (by salary):")
for f in sorted_faculty:
    print(f.name, f.salary)


# -------- 3. Filtered Data --------
print("\n--- FILTERED ---")

high_fee = list(filter(lambda s: s.fees > 50000, students))
high_salary = list(filter(lambda f: f.salary > 30000, faculty))

print("\nHigh Fee Students:")
for s in high_fee:
    print(s.name, s.fees)

print("\nHigh Salary Faculty:")
for f in high_salary:
    print(f.name, f.salary)


# -------- 4. Total (reduce) --------
print("\n--- TOTALS ---")

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees:", total_fees)
print("Total Salary:", total_salary)