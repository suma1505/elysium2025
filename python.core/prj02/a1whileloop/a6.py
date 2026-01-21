i = 1
while i < 10:
    i += 1
    if i < 6:
        continue
    print(i)
else:
    print('while loop ends with:', i, 'value')
print('i value (outside of loop):',i)
'''
6
7
8
9
10
while loop ends with: 10 value
i value (outside of loop): 10
'''