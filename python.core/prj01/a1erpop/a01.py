rno = int(input('Enter roll no:'))
sname = str(input('Enter student name:'))
m1 = float(input('Enter mark 1:'))
m2 = float(input('Enter mark 2:'))
print(rno, type(rno))
print(sname, type(sname))
print(m1, type(m1))
print(m2, type(m2))
rno = int(rno)
m1 = float(m1)
m2 = float(m2)
print(rno, type(rno))
print(m1, type(m1))
print(m2, type(m2))
total = m1 + m2
avg = total / 2
if m1 > 34.4 and m2 > 34.4:
    result = 'pass'
else:
    result = 'fail'
print('Roll no:', rno)
print('Student name:', sname)
print('Mark 1:', m1)
print('Mark 2:', m2)
print('Total:', total)
print('Average:', avg)
print('Result:', result)
'''
Enter roll no:1001
Enter student name:x3
Enter mark 1:56.5
Enter mark 2:63
1001 <class 'int'>
x3 <class 'str'>
56.5 <class 'float'>
63.0 <class 'float'>
1001 <class 'int'>
56.5 <class 'float'>
63.0 <class 'float'>
Roll no: 1001
Student name: x3
Mark 1: 56.5
Mark 2: 63.0
Total: 119.5
Average: 59.75
Result: pass
'''