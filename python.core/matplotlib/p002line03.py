from matplotlib import pyplot as plt

rno = [1001, 1002, 1003]
fine = [50.00, 10.00, 30.00]
plt.xlabel('Roll No.')
plt.ylabel('Fine Rs.')
plt.plot(rno, fine, marker='o')
plt.show()
