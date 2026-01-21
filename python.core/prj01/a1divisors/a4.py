def uDivisors(n):
    return [i for i in range(1, n) if n % i == 0]
def uIsDeficientNumber(n):
    ds = uDivisors(n)
    sods = sum(ds)
    return True if sods < n else False
for x in range(1, 51):
    if uIsDeficientNumber(x):
        print(x)
'''
1
2
3
4
5
7
8
9
10
11
13
14
15
16
17
19
21
22
23
25
26
27
29
31
32
33
34
35
37
38
39
41
43
44
45
46
47
49
50
'''