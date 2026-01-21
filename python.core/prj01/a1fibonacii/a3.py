def fibonacciValue(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r
sf = 0
s = input("enter x value:")
for ch in s:
    sf += fibonacciValue(int(ch))
    if s == str(sf):
        print(f"{s} is strong number")
    else:
        print(f"{s} is not strong number")
'''
enter x value:145
145 is not strong number
145 is not strong number
145 is strong number
'''