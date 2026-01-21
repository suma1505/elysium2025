def fibonaciiValue(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r
for m in range(1, 1001):
    sf = 0
    s = str(m)
    for ch in s:
        sf += fibonaciiValue(int(ch))
        if s == str(sf):
            print(f"{s} is strong number")
'''
1 is strong number
2 is strong number
145 is strong number
'''