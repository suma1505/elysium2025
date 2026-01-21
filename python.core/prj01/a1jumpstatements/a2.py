for i in range(1, 11):
    if i == 6:
        continue
    print(i)
else:
    print('for each loop ends here')
print('outside of for loop i variable value:', i)
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
for each loop ends here
outside of for loop i variable value: 10
'''