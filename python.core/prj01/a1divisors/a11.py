from math import sqrt, floor
def uDivisors(n):
    return [i for i in range(1, n)if (n % i)==0]
M = 48
N = 75
d1 = uDivisors(M)
s1 = sum(d1)
d2 = uDivisors(N)
s2 = sum(d2)
print(M, ":", d1, "=", s1)
print(N, ":", d2, "=", s2)
if (M + 1) == s2 and (N + 1) == s2:
    print(f"\n({M}, {N}) number are betrothed numbers")
else:
    print(f"\n({M}, {N}) number are not betrothed numbers")
'''
  48 : [1, 2, 3, 4, 6, 8, 12, 16, 24] = 76
75 : [1, 3, 5, 15, 25] = 49

(48, 75) number are not betrothed numbers  
'''