def uSum(i, j):
    return i + j
def uMinus(x, y):
    print(("{0} - {1} = {2}".format(x, y, x - y)))
    return
print(uSum(2, 5))
a, b = 3, 6
print(uSum(a, b))
m = uSum(3, 2)
print('m:', m)
n = uSum(b, b)
print('n:', n)
uMinus(18, 4)
a, b = 3, 2
uMinus(a, b)
'''
7
9
m: 5
n: 12
18 - 4 = 14
3 - 2 = 1
'''