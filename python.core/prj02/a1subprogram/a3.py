def uShow(startv, stopv, stepv):
    for i in range(startv, stopv + 1, stepv):
        print(i)
    return
uShow(1, 10, 1)
uShow(1, 10, 2)
uShow(1, 100, 10)
'''
output 1
1
2
3
4
5
6
7
8
9
10
output 2
1
3
5
7
9
output 3
1
11
21
31
41
51
61
71
81
91
'''