from numpy import *
ar1 = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
ar2 = asmatrix(ar1)
print(ar1)
print(ar2)
ar2[1,1]=0
print(ar1)
print(ar2)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 2 3]
 [4 0 6]
 [7 8 9]]
[[1 2 3]
 [4 0 6]
 [7 8 9]]

'''