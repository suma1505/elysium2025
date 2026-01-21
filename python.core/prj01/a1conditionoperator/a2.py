i, j, k = 5, 9, 7
print("i={0}, j={1}, k={2}".format(i, j, k))
if i > j:
    if i > k:
        print('i:', i)
    else:
        print('k:', k)
else:
    if j > k:
        print('j:', j)
    else:
        print('k:', k)
'''
i=5, j=9, k=7
j: 9
'''