class Salary:
    def setData(self):
        self.eid = int(input('Enter emp no:'))
        self.ename = input('Enter emp name:')
        self.sal = float(input('Enter sal:'))
        return
    def computeData(self):
        self.hra = self.sal * 20 / 100
        self.da = self.sal * 15 / 100
        self.pf = self.sal * 35 / 100
        self.gpay = self.sal + self.hra + self.da
        self.npay = self.gpay - self.pf
        return
    def showData(self):
        self.computeData()
        print('employee id:', (self.eid))
        print('employee name:', (self.ename))
        print('employee sal:', (self.sal))
        print('house rent allowance:', (self.hra))
        print('dearness allowance:', (self.da))
        print('provident fund:', (self.pf))
        print('gross pay:', (self.gpay))
        print('net pay:', (self.npay))
obj = Salary()
obj.setData()
obj.showData()
'''
Enter sal:100000
employee id: 1001
employee name: X5
employee sal: 100000.0
house rent allowance: 20000.0
dearness allowance: 15000.0
provident fund: 35000.0
gross pay: 135000.0
net pay: 100000.0
'''





