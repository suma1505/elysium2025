from numpy import *
ar1 = arange(1,6)
ar2 = arange(5,10)
print(ar1)
print(ar2)
print(add(ar1, ar2))
print(multiply(ar1, ar2))
print(subtract(ar2, ar1))
print(divide(ar2, ar1))
print(remainder(ar2, ar1))
print(square(ar2))

'''
[1 2 3 4 5]
[5 6 7 8 9]
[ 6  8 10 12 14]
[ 5 12 21 32 45]
[4 4 4 4 4]
[5.         3.         2.33333333 2.         1.8       ]
[0 0 1 0 4]
[25 36 49 64 81]
'''