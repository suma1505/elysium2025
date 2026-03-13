from numpy import *
ar = arange(15).reshape(3,5)
print(ar)
print(average(ar))
print(median(ar))
print(mean(ar))

print(average(ar,axis=0))
print(median(ar,axis=0))
print(mean(ar,axis=0))

print(average(ar,axis=1))
print(median(ar,axis=1))
print(mean(ar,axis=1))
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
7.0
7.0
7.0
[5. 6. 7. 8. 9.]
[5. 6. 7. 8. 9.]
[5. 6. 7. 8. 9.]
[ 2.  7. 12.]
[ 2.  7. 12.]
[ 2.  7. 12.]
'''