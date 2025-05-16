mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry
# StopIteration exception will be raised if there are no more items


mystr = "banana"
myit = iter(mystr)
print(next(myit))  # b
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a

mydict = {"name": "John", "age": 36, "country": "Norway"}
myit = iter(mydict)
print(next(myit))  # name
print(next(myit))  # age
print(next(myit))  # country

