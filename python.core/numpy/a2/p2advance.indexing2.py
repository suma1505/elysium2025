from numpy import *
ar = array([[1,2],[3,4],[5,6]])
print(ar)
print(ar[[0],[1]]+1)
ar[[0],[1]]+=1
print(ar)
'''
[[1 2]
 [3 4]
 [5 6]]
[3]
[[1 3]
 [3 4]
 [5 6]]
'''