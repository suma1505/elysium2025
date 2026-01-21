def uFibonacciSeries(n):
    i = 1
    r = 1
    while i <= n:
        r *= i
        i += 1
    return r
print(uFibonacciSeries(5))
'''
120
'''