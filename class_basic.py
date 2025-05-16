class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p2 = Person("Jane", 28)
print(p1.name)
print(p2.age)
print(p1.age)
print(p2.name)