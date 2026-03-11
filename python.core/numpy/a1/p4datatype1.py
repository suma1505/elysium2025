from numpy import *
ari = array([1,2,3,])
arf1 = array([0.1,0.2,0.3])
arf2 = array([1,2,3],float)
arb1 = array([False,True])
ars1 = array(["sun", "mon", "tue", "wed"])
arc1 = array([1+2j, 3+4j, 5+6*7j])
print(ari)
print(ari.dtype)

print(arf1)
print(arf1.dtype)

print(arf2)
print(arf2.dtype)

print(arb1)
print(arb1.dtype)

print(ars1)
print(ars1.dtype)

print(arc1)
print(arc1.dtype)

'''
[1 2 3]
int64
[0.1 0.2 0.3]
float64
[1. 2. 3.]
float64
[False  True]
bool
['sun' 'mon' 'tue' 'wed']
<U3
[1. +2.j 3. +4.j 5.+42.j]
complex128
'''