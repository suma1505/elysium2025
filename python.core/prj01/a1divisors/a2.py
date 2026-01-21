def uDivisors(n):
    r = []
    for i in range(1, n):
        if n % i == 0:
            r.append(i)
    return r
def uIsDeficientNumber(n):
    ds = uDivisors(n)
    sods = sum(ds)
    return True if sods < n else False
print(21, uIsDeficientNumber(21))
'''
21 True
'''