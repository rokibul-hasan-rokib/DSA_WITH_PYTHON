def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search_recursive(arr, target, 0, len(arr) - 1)


print(f"Target found at index: {result}" if result != -1 else "Target not found")
