def uDivisors(n):
    return [i for i in range(1, n) if n % i == 0]
def uAbuDefPer(n):
    ds = uDivisors(n)
    sods = sum(ds)
    if sods < n:
        return 'deficient number'
    elif sods > n:
        return 'abundant number'
    else:
        return 'perfect number'
print(6, uAbuDefPer(6))
print(7, uAbuDefPer(7))
print(12, uAbuDefPer(12))
'''
6 perfect number
7 deficient number
12 abundant number
'''