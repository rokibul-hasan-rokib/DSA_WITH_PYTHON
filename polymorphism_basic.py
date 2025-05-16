class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def move(self):
        print("The car is moving")

class Truck(Car):
    def __init__(self, name, model, color, capacity):
        super().__init__(name, model, color)
        self.capacity = capacity

    def move(self):
        print("The truck is moving with a capacity of", self.capacity)

class Bike(Car):

    def __init__(self, name, model, color, type):
        super().__init__(name, model, color)
        self.type = type

    def move(self):
        print("The bike is moving with type", self.type)

class Bus(Car):
    def __init__(self, name, model, color, seats):
        super().__init__(name, model, color)
        self.seats = seats

    def move(self):
        print("The bus is moving with", self.seats, "seats")    

class Vehicle:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def move(self):
        print("The vehicle is moving")