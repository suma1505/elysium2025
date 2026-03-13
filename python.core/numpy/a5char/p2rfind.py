from numpy import *
ar = array(['ababab', 'abcabc', 'ABCabcABCabc'])
print(char.rfind(ar, 'ab'))
print(char.rfind(ar, 'abc'))
print(char.rfind(ar, 'ABC'))
'''
[4 3 9]
[-1  3  9]
[-1 -1  6]
'''