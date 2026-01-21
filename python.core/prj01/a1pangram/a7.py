def uReverseNumber(n):
    r = 0
    t = n
    d = 0
    while t > 0:
        d = t % 10
        r = (r * 10) + d
        t = t // 10
    return r
print(uReverseNumber(4321))
'''
1234
'''