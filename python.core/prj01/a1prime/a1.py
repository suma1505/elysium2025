def isPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
x = 10
if isPrimeNumber(x):
    print(f"{x} is prime number")
else:
    print(f"{x} is not prime number")
x = 13
if isPrimeNumber(x):
    print(f"{x} is prime number")
else:
    print(f"{x} is not prime number")
'''
10 is not prime number
13 is prime number
'''