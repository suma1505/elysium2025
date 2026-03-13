from numpy import *
ar = array([
    [1,3,0],
    [5,0,0],
    [0,7,9]
])
print(ar)
print(count_nonzero(ar))
print(count_nonzero(ar,axis=None))
print(count_nonzero(ar,axis=0))
print(count_nonzero(ar,axis=1))
'''
[[1 3 0]
 [5 0 0]
 [0 7 9]]
5
5
[2 2 1]
[2 1 2]
'''
