from numpy import *
ar =array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0,1,2]
])
print(ar)
for x in ar:
    print(x)
    for x,y,z in ar:
        print(x+y+z)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]
 [0 1 2]]
[1 2 3]
6
15
24
3
[4 5 6]
6
15
24
3
[7 8 9]
6
15
24
3
[0 1 2]
6
15
24
3
'''