def uFibonacciSeries(n):
    if n == 1:
        return n
    else:
        return n * uFibonacciSeries(n - 1)
print(uFibonacciSeries(4))
'''
24
'''