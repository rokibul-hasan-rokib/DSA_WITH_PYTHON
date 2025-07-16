class Parent:
    def method(self):
        print("Parent method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

Child1().method()
Child2().method()
