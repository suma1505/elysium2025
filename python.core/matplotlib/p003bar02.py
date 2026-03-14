from matplotlib import pyplot as plt
sname = [1001,1002,1003,1004,1005]
fine = [10.00, 30.00, 50.00, 20.00, 40.00]
plt.bar(sname, fine)
plt.title('Regarding: Fine Amount')
plt.xlabel('Student Name')
plt.ylabel('Fine Rs')
plt.bar(sname,fine,color='red', width=0.1, align='center')
plt.show()
plt.bar(sname,fine,color='red', width=0.1, align='edge')
plt.show()