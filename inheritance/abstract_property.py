from abc import ABC, abstractmethod
class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @classmethod
    @abstractmethod
    def create(cls):
        pass

class Circle(Shape):
    @property
    def name(self):
        return "Circle"

    @classmethod
    def create(cls):
        return cls()

circle = Circle()
print(circle.name)
