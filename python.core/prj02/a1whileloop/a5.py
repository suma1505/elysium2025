i = 1
while i < 10:
    if i == 6:
        break
    print(i)
    i += 1
else:
    print('while loop ends with', i, 'value')
print('i value (outside of loop):', i)
'''
1
2
3
4
5
i value (outside of loop): 6
'''