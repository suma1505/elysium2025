from numpy import *
ar = array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
print(ar)
for x in ar:
    print(x)
for x,y in ar:
    print(x+y)

'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
[1 2]
[3 4]
[5 6]
[7 8]
3
7
11
15
'''