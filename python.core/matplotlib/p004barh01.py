from matplotlib import pyplot as plt
sname = ['x1', 'x2', 'x3', 'x4', 'x5']
fine = [50.00, 30.00, 10.00, 20.00, 40.00]
plt.title('Regarding Fine Amount')
plt.xlabel('Fine Rs')
plt.ylabel('Student Name')
plt.barh(sname,fine,color='red', height=0.5)
plt.show()
plt.barh(sname,fine,color='red', height=0.5, align='edge')
plt.show()