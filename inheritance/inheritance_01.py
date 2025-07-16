class Animal:
    def rokib(self):
        print("Subclass must implement this method")
        
class Dog(Animal):
    def speak(self):
        print("Woof Woof")
        
class Cat(Animal):
    def speak(self):
        print("Meow Meow")
        
dog = Dog()
cat = Cat()

dog.speak()
dog.rokib()
cat.speak()
    
    