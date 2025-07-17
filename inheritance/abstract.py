from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def move(self):
        print("I can move")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak() 