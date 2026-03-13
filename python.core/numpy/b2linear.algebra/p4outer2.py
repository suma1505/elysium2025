from numpy import array
from numpy.ma.core import outer

x = [[0,1,2],[3,4,5]]
y = [[1,1,1],[1,1,1]]
z = outer(x,y)
print(x)
print(y)
print(z)
'''
[[0, 1, 2], [3, 4, 5]]
[[1, 1, 1], [1, 1, 1]]
[[0 0 0 0 0 0]
 [1 1 1 1 1 1]
 [2 2 2 2 2 2]
 [3 3 3 3 3 3]
 [4 4 4 4 4 4]
 [5 5 5 5 5 5]]
'''