def sum_list(numbers):
    if not numbers:
        return 0;
    else:
        return numbers[0] + sum_list(numbers[1:])
    
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(result)