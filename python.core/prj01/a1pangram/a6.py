def uReverseNumber(n):
    r = 0
    t = n
    d = 0
    while t > 0:
        d = t % 10
        r = (r * 10) + d
        t = t // 10
    return r
i = 1221
j = uReverseNumber(i)
if i == j:
    print(f"{i} is palindrome")
else:
    print(f"{i} is not palindrome")
i = 123
j = uReverseNumber(i)
if i == j:
    print(f"{i} is palindrome")
else:
    print(f"{i} is not palindrome")
'''
1221 is palindrome
123 is not palindrome
'''