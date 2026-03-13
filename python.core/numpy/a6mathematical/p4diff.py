from numpy import *
ar = array([[2,6],[7,9]])
print(diff(ar))
print(diff(ar,axis =0))
print(diff(ar,axis = 1))
'''
[[4]
 [2]]
[[5 3]]
[[4]
 [2]]
'''