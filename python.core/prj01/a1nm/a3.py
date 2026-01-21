def uSumOfDigits(s):
    r = 0
    for ch in s:
        r = r + int(ch)
    return r
x = input("enter x avalue:")
print(uSumOfDigits(x))
'''
enter x avalue:12345
15
'''