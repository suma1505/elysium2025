from math import sqrt,floor
def uIsPerfectSquare(n):
    sr = sqrt(n)
    if (sr - floor(sr)) == 0:
        return True
    else:
        return False
for x in range(0, 10):
    if uIsPerfectSquare(x):
        print(x)
'''
0
1
4
9
'''