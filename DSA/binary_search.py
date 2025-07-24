def binarySearch(arr, targetVal):
    left  = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            return mid
        elif arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1

mylist = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binarySearch(mylist, target)
print(f"Target found at index: {result}" if result != -1 else "Target not found")