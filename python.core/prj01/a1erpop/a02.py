m1 = m2 = 0
try:
    m1 = float(input('Enter mark 1:'))
except Exception as e:
    print('error:', e)
    m1 = 0
try:
    m2 = float(input('Enter mark 2:'))
except Exception as e:
    print('error:', e)
    m2 = 0
print(f'mark 1:, {m1}\nmark 2:, {m2}\ntotal:', m1 + m2)
'''
input 1
Enter mark 1:56.5
Enter mark 2:63
output 1
mark 1:, 56.5
mark 2:, 63.0
total: 119.5
input 2
Enter mark 1:orange
error: could not convert string to float: 'orange'
Enter mark 2:63
output 2
mark 1:, 0
mark 2:, 63.0
total: 63.0
input 3
Enter mark 1:1.3.5.7.9
error: could not convert string to float: '1.3.5.7.9'
Enter mark 2:fox
error: could not convert string to float: 'fox'
]output 3
mark 1:, 0
mark 2:, 0
total: 0
'''


