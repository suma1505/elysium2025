from numpy import *
ar = arange(15).reshape(3,5)
print(ar)
print(amin(ar))
print(amax(ar))
print(amin(ar,axis=0))
print(amax(ar,axis=0))
print(amin(ar,axis=1))
print(amax(ar,axis=1))
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
0
14
[0 1 2 3 4]
[10 11 12 13 14]
[ 0  5 10]
[ 4  9 14]
'''