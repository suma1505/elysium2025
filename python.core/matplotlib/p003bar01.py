from matplotlib import pyplot as plt
rno = [1001,1002,1003,1004,1005]
fine = [10.00, 30.00, 50.00, 20.00, 40.00]
plt.bar(rno, fine)
plt.title('Regarding: Fine Amount')
plt.xlabel('Rno No')
plt.ylabel('Fine Rs')
plt.show()