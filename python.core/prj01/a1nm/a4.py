def uSumOfDigits(n):
    sd = 0
    while n > 0:
        r = int(n % 10)
        sd += r
        n = n / 10
    return sd
x = 9876
print(uSumOfDigits(x))
'''
30
'''