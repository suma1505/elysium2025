from matplotlib import pyplot as plt
sname = ['x5', 'x3', 'x1', 'x2', 'x4']
fees = [200.00, 400.00, 100.00, 500.00, 300.00]
plt.plot(sname, fees, marker='o')
plt.title('Regarding: Fees Amount')
plt.xlabel('Student Name.')
plt.ylabel('Fees Amount.')
plt.grid(True)
plt.show()
