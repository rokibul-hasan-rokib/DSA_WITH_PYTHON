class Person:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age

    def myFunction(mySillyObject):
        print("Hello my name is " + mySillyObject.name)

p1 = Person("John", 36)
p2 = Person("Jane", 28)
print(p1.name)
print(p2.age)
print(p1.age)
print(p2.name)
p1.myFunction()
p2.myFunction()