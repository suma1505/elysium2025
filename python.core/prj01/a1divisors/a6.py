def uDivisors(n):
    r = []
    for i in range(1, n):
        if n % i == 0:
            r.append(i)
    return r
x = 6
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
x: 6
y: [1, 2, 3]
z: 6
6 is perfect number
'''