def uArmstrongNumber(n):
    ts = str(n)
    pn = len(ts)
    sd = 0
    for ch in ts :
        sd += int(ch) ** pn
        return True if n == sd else False
i = 1634
if uArmstrongNumber(i):
    print(i, "is armstrong number")
else:
    print(i, "is not armstrong number")
'''
1634 is not armstrong number
'''