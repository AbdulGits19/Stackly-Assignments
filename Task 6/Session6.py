# # Task 1: Encapsulation (User Class)

class User:

    def __init__(self):

        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):

        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return f'Username : {self.__user_name}'
    
    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        usr = input('Enter Username : ')
        passw = input('Enter Password : ')

        if usr == self.__user_name and passw == self.__pwd:
            print(f"Logging in: {self.__user_name}")
        else:
            print('Wrong Credentials, Try Again!')


user1 = User()
user1.set_user('Abdul','PythonTask6@123')
user1.register()
print(user1.get_user())
user1.login()


# Task 2: Inheritance (User → Student, Faculty)


class User:
    def register(self):
        print("User registered")

    def login(self):
        print("User logged in")

class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


test = TempFaculty()

test.register()           # This is inherited from grandparent
test.faculty_greet()      # This is inherited from direct parent
test.tempFaculty_greet()  # This is an own method


# # Task 3: Method Overriding


class User:
    def greet(self):
        print("Welcome User")


class Student(User): # First Child

    def greet(self): #Overriding 
        print("Welcome Student")


class Faculty(User): #Second Child

    def greet(self): #Overriding again
        print("Welcome Faculty")


avg_user = User()
student = Student()
faculty = Faculty()


# Object call

avg_user.greet() # Welcome User
student.greet()  # Welcome Student
faculty.greet()  # Welcome Faculty


# # Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self 

    def login(self):
        print("logged in")
        return self  

    def greet(self):
        print("enjoy everyone")
        return self  


user1 = User()
user1.register().login().greet()


#  Task 5: Combined Task (Real-Time)


class User:
    users_count = 0 

    def __init__(self, username, pwd):
        self.__user_name = username
        self.__pwd = pwd
        User.users_count += 1

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"registered: {self.__user_name}")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("Welcome User")
        return self
    
# Method overriding classes....

class Student(User):

    def greet(self):
        print("Welcome Student")
        return self

class Faculty(User):
    # Method Overriding
    def greet(self):
        print("Welcome Faculty")
        return self


u1 = Student("abdul_19", "random@786")
u2 = Faculty("karun_s", "karunakar@178")

print(f"Total Users Created: {User.users_count}\n")

print("--- Student Chain ---")
u1.login().greet().register()

print("\n--- Faculty Chain ---")
u2.login().greet().register()