from numpy import *
x = [[1,2],[3,4]]
y = [[1,1],[1,1]]
z = outer(x,y)
print(x)
print(y)
print(z)
'''
[[1, 2], [3, 4]]
[[1, 1], [1, 1]]
[[1 1 1 1]
 [2 2 2 2]
 [3 3 3 3]
 [4 4 4 4]]
'''