def uArmstrongNumber(n):
    pn = len(str(n))
    tn = n
    r = 0
    sd = 0
    while tn > 0:
        r = tn % 10
        tn = tn // 10
        sd += (r ** pn)
    if n == sd:
        return True
    else:
        return False
i = 153
if uArmstrongNumber(i):
    print(f"{i} is armstrong number")
else:
    print(f"{i} is not armstrong number")
'''
153 is armstrong number
'''