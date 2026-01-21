def uDivisors(n):
    return [i for i in range(1, n) if n % i ==0]
x = 18
y = uDivisors(x)
z = sum(y)
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
if x == z:
    print(f"{x} is perfect number")
else:
    print(f"{x} is not perfect number")
'''
x: 18
y: [1, 2, 3, 6, 9]
z: 21
18 is not perfect number
'''