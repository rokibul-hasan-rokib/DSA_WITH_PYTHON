class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "Animal Speaking"
    
class Dog(Animal):
    def speak(self):
        return "Woof Woof"
    
a = Animal("Animal")
b = Dog("Dog")

print(a.speak())
print(b.speak())