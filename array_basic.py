cars = ["Ford", "Chevy", "Toyota", "Honda"] 
x = len(cars)
print(x)

cars.append("BMW")

print(cars)

for x in cars:
    print(x)

cars.remove("Chevy")
print(cars)
cars.pop(0)
car.pop(1)