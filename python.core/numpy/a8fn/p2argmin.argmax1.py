from numpy import *
ar = array([
    [1,7,2],
    [6,3,4],
    [9,8,5]
])
print(ar)
print(argmin(ar))
print(argmin(ar,axis=None))
print(argmax(ar))
print(argmax(ar,axis=None))
'''
[[1 7 2]
 [6 3 4]
 [9 8 5]]
0
0
6
6
'''