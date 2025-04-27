def countDown(n):
    if n == 0:
        return 0
    else:
        print(n)
        return countDown(n-1)
    
countDown(10)