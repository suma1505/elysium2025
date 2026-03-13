from numpy import *
ar = array([[1,2,3],[4,5,6],[7,8,9]])
print(ar)
print(ar[ar == 5])
print(ar[ar == 55])
print(ar[ar%2 != 0])
print(ar[ar%2 == 0])
print(ar[ar > 5])

'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[5]
[]
[1 3 5 7 9]
[2 4 6 8]
[6 7 8 9]
'''