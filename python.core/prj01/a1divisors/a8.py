def uDivisors(n):
    return [i for i in range(1, n) if n % i == 0]
for x in range(1, 1001):
    y = uDivisors(x)
    z = sum(y)
    if x == z:
        print(f"{x} is perfect number")
'''
6 is perfect number
28 is perfect number
496 is perfect number
'''