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
for i in range(1001):
    if uArmstrongNumber(i):
        print(f"{i} is armstrong number")
'''
1 is armstrong number
2 is armstrong number
3 is armstrong number
4 is armstrong number
5 is armstrong number
6 is armstrong number
7 is armstrong number
8 is armstrong number
9 is armstrong number
25 is armstrong number
36 is armstrong number
125 is armstrong number
216 is armstrong number
729 is armstrong number
'''