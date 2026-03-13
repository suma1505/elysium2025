from numpy import *
x = char.equal('sun', 'sun')
print(x)
x = char.equal('sun', 'SUN')
print(x)
x = char.not_equal('sun', 'sun')
print(x)
x = char.not_equal('sun', 'SUN')
print(x)
'''
True
False
False
True
'''