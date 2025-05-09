list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = list1 + list2

print(list3)  # Output: [1, 2, 3, 'a', 'b', 'c']

for x in list2:
    list1.append(x)

print(list1) # Output: [1, 2, 3, 'a', 'b', 'c']


list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 'a', 'b', 'c', 'a', 'b', 'c']


 