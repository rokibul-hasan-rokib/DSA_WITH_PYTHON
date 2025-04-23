number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
number3 = int(input("Enter another number: "))  

if(number1 > number2 and number1 > number3):
    print("The largest number is", number1)
elif(number2 > number1 and number2 > number3):
    print("The largest number is", number2)
else:
    print("The largest number is", number3)