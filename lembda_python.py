x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

def myFuncf(n):
    return lambda a : a * n

mydoubler = myFuncf(2)

print(mydoubler(11))