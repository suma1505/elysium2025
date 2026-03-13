from numpy import *
ar = array(['sun', 'sunset', 'sunrise coffee'])
print(char.count(ar, 'sun'))
print(char.count(ar, 'set'))
print(char.count(ar, 'rise'))
print(char.count(ar, 'sunrise'))
print(char.count(ar, 'coffee'))
'''
[1 1 1]
[0 1 0]
[0 0 1]
[0 0 1]
[0 0 1]
'''