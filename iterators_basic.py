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

for x in mytuple:
    print(x)  # apple, banana, cherry


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)  # 1, 2, 3, 4, 5, 6, 7, 8, 9
# StopIteration exception will be raised if there are no more items
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))