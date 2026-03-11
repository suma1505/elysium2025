from numpy import *
ar = array([[1,1.5,2,2.5],
            [3,3.5,4,4.5],
            [5,5.5,6,6.5],
            [7,7.5,8,8.5]],float)
print(ar)
print(len(ar))
print(ar.ndim)
print(ar.shape)
print(type(ar))
print(ar.dtype)

print(ar[0])
print(ar[1])
print(ar[2])

print(ar[0,0])
print(ar[1,2])
print(ar[2,2])
print(ar[3,3])

'''
[[1.  1.5 2.  2.5]
 [3.  3.5 4.  4.5]
 [5.  5.5 6.  6.5]
 [7.  7.5 8.  8.5]]
4
2
(4, 4)
<class 'numpy.ndarray'>
float64
[1.  1.5 2.  2.5]
[3.  3.5 4.  4.5]
[5.  5.5 6.  6.5]
1.0
4.0
6.0
8.5
'''