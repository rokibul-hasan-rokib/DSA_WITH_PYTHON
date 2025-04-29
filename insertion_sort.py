numbers=[2,1,5,4,3]
for i in range(1,len(numbers)):
    j=i-1
    while j>=0 and numbers[j]>numbers[j+1]:
        numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
        j-=1

print(numbers)