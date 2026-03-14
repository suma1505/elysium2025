from matplotlib import pyplot as plt

sname = ['x1','x2', 'x3']
fees = [300.00, 100.00, 500.00]
plt.xlabel('Student Name.')
plt.ylabel('Fees Rs')
plt.plot(sname, fees, marker='^')
plt.show()