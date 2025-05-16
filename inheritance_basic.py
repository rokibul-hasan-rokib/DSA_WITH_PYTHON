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