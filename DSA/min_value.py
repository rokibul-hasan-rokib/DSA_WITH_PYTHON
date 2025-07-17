arrayValue = [ 6, 9, 8, 5, 10]

minValue = arrayValue[0]

for i in arrayValue:
    if i < minValue:
        minValue = i

print('Minimum value is: ',minValue)