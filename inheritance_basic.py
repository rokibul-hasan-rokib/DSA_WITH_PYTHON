class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printname(self):
        print("Hello my name is " + self.firstname + " " + self.lastname)

x = Person("John", "Doe", 36)
y = Person("Jane", "Doe", 28)
x.printname()

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname, age)
        self.graduationyear = 2023

    def welcome(self):
        print("Welcome " + self.firstname + " " + self.lastname + " to the class of " + str(self.graduationyear))

x = Student("John", "Doe", 36)
y = Student("Jane", "Doe", 28)
x.welcome()
y.welcome()
