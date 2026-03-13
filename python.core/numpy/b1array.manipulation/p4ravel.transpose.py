from numpy import *
ar = arange(4*3*2)
print(ar)
print(ar.shape)
ar =ar.reshape(4,3,2)
print(ar)
print(ar.shape)
'''
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
(24,)
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]

 [[12 13]
  [14 15]
  [16 17]]

 [[18 19]
  [20 21]
  [22 23]]]
(4, 3, 2)
'''