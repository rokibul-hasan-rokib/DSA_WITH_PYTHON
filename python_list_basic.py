thisList = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(thisList)

thisList = ['apple', 'banana', 'cherry']
print(len(thisList))

thisList = ['apple', 'banana', 'cherry']
print(thisList[1])

thisList = ['apple', 'banana', 'cherry']
print(thisList[-1])

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[2:5])

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[:4])

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[2:])

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[-4:-1])

thisList = ['apple', 'banana', 'cherry']
if 'apple' in thisList:
    print("Yes, 'apple' is in the fruits list")

thisList = ['apple', 'banana', 'cherry']
thisList[1] = 'blackcurrant'
print(thisList)

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
thisList[1:3] = ['blackcurrant', 'watermelon']
print(thisList)

thisList = ['apple', 'banana', 'cherry']
thisList.insert(2, 'watermelon')
print(thisList)

thisList = ['apple', 'banana', 'cherry']
thisList.append('orange')
print(thisList)

thisList = ['apple', 'banana', 'cherry']
thisList.insert(1, 'orange')
print(thisList)

thisList = ['apple', 'banana', 'cherry']
thisList.remove('banana')
print(thisList)

thisList = ['apple', 'banana', 'cherry']
thisList.pop(1)
print(thisList)

thisList = ['apple', 'banana', 'cherry']
thisList.clear()
print(thisList)

thisList = ['apple', 'banana', 'cherry']
del thisList
print(thisList)

mylist = ['apple', 'banana', 'cherry']
mylist2 = mylist.copy()
print(mylist2)

mylist = ['apple', 'banana', 'cherry']
mylist2 = list(mylist)
print(mylist2)

mylist = ['apple', 'banana', 'cherry']
print(type(mylist))