import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(type(arr))

arr1 = np.array([1, 2, 3, 4])

print(arr1[2] + arr1[3])

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[0, 1, 2])