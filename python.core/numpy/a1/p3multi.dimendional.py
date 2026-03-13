from numpy import *
def show(ar):
    print(ar)
    print(len(ar))
    print(ar,ndim)
    print(ar.shape)
    print(type(ar))
    print(ar.dtype)
    print('-' * 80)
    return
arr = array([[11,22,33,44],[55,66,77,88]])
show(arr)
arr=array([[11,22,33,44],[55,66,77,88]],float)
show(arr)
'''
[[11 22 33 44]
 [55 66 77 88]]
2
[[11 22 33 44]
 [55 66 77 88]] <function ndim at 0x000002AF64B322A0>
(2, 4)
<class 'numpy.ndarray'>
int64
--------------------------------------------------------------------------------
[[11. 22. 33. 44.]
 [55. 66. 77. 88.]]
2
[[11. 22. 33. 44.]
 [55. 66. 77. 88.]] <function ndim at 0x000002AF64B322A0>
(2, 4)
<class 'numpy.ndarray'>
float64
'''