from numpy import *
ar = array(['sun', 'sunset', 'sunrise coffee'])
print(char.find(ar, 'sun'))
print(char.find(ar, 'set'))
print(char.find(ar, 'rise'))
print(char.find(ar, 'sunrise'))
print(char.find(ar, 'coffee'))
'''
[0 0 0]
[-1  3 -1]
[-1 -1  3]
[-1 -1  0]
[-1 -1  8]
'''