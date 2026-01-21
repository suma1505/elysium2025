def uStr2Float(fpa):
    try:
        fpa = float(fpa)
    except Exception as e:
        fpa = 0
        print('Err:', e)
    return fpa
print("\nEnter value for marks...")
m1 = input('mark 1:')
m2 = input('mark 2:')
m3 = input('mark 3:')
print(m1 + m2 + m3,"\n")
m1 = uStr2Float(m1)
m2 = uStr2Float(m2)
m3 = uStr2Float(m3)
total = m1 + m2 + m3
avg = total / 3
result = 'pass' if m1 >34.4 and m2 > 34.4 and m3 > 34.4 else 'fail'
print('total:', total)
print('average:', avg)
print('result:', result)
'''
Enter value for marks...
mark 1:54.5
mark 2:61
mark 3:79.5
54.56179.5 

total: 195.0
average: 65.0
result: pass
output 2
Enter value for marks...
mark 1:fox
mark 2:dog
mark 3:79.5
foxdog79.5 

Err: could not convert string to float: 'fox'
Err: could not convert string to float: 'dog'
total: 79.5
average: 26.5
result: fail
'''