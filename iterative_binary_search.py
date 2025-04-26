def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) 
        
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  

arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search_iterative(arr, target)
print(f"Target found at index: {result}" if result != -1 else "Target not found")
