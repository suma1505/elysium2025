class Calc:
    def setData(self):
        self.x = int(input('Enter x value:'))
        self.y = int(input('Enter y value'))
        return
    def uSum(self):
        print(self.x + self.y)
        return
    def uMinus(self):
        return self.x - self.y
    def uDiv(self):
        print(self.x / self.y)
        return
    def uMod(self):
        return self.x % self.y
obj = Calc()
obj.setData()
obj.uSum()
print(obj.uMinus())
obj.uDiv()
print(obj.uMod())
'''
Enter x value:5
Enter y value3
8
2
1.6666666666666667
2
'''