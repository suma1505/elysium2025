from matplotlib import pyplot as plt
sname = ['x1', 'x2', 'x3', 'x4']
m1 = [90, 70, 50, 30]
m2 = [30, 50, 70, 90]
m3 = [70, 90, 30, 50]
b1, b2, b3, b4 = [], [], [], []
for x in range(len(m1)):
    b1.append(x)
for x in b1:
    b2.append(x + 0.25)
for x in b2:
    b3.append(x + 0.25)
for x in b3:
    b4.append(x + 0.25)
plt.bar(b1, m1, width=0.25, color='r', edgecolor='white', label='Mark-1')
plt.bar(b2, m2, width=0.25, color='g', edgecolor='white', label='Mark-2')
plt.bar(b3, m3, width=0.25, color='b', edgecolor='white', label='Mark-3')
plt.xlabel('Student Name', fontweight='bold', fontsize=14)
plt.xlabel('Marks', fontweight='bold', fontsize=14)
b5 = []
b5.extend(m1)
b5.extend(m2)
b5.extend(m3)
print(b5)
b5 = list(set(b5))
print(b5)
plt.xticks(ticks=b4, labels=sname)
plt.legend()
plt.show()

