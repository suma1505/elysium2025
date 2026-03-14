from matplotlib import pyplot as plt
rno = [1001, 1002, 1002, 1004, 1005]
fine = [10.00, 30.00, 50.00, 20.00, 40.00]
plt.plot(rno, fine, marker='o')
plt.title('Regarding: Fine Amount')
plt.xlabel('Roll No.')
plt.ylabel('Fine Rs.')
plt.show()
