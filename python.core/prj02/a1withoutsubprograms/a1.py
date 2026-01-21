print("\nEnter value for marks...")
m1 = input('mark 1:')
m2 = input('mark 2:')
m3 = input('mark 3:')
print(m1 + m2 + m3, "\n")
try:
    m1 = float(m1)
except Exception as e:
    m1 = 0
    print('Err:', e)
try:
    m2 = float(m2)
except Exception as e:
    m2 = 0
    print('Err:', e)
try:
    m3 = float(m3)
except Exception as e:
    m3 = 0
    print('Err:', e)
total = m1 + m2 + m3
avg = total / 3
result = 'pass' if m1 > 34.4 and m2 > 34.4 and m3 >34.4 else 'fail'
print('mark 1:', m1)
print('mark 2:', m2)
print('mark 3:', m3)
print('total:', total)
print('average:', avg)
print('result:', result)
'''
Enter value for marks...
mark 1:56.5
mark 2:79
mark 3:45.5
56.57945.5 

mark 1: 56.5
mark 2: 79.0
mark 3: 45.5
total: 181.0
average: 60.333333333333336
result: pass
output 2
Enter value for marks...
mark 1:sun
mark 2:mon
mark 3:tue
sunmontue 

Err: could not convert string to float: 'sun'
Err: could not convert string to float: 'mon'
Err: could not convert string to float: 'tue'
mark 1: 0
mark 2: 0
mark 3: 0
total: 0
average: 0.0
result: fail
'''