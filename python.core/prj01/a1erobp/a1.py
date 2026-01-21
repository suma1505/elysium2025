class ExamResult:
    def setData(self):
        self.rno = int(input('Enter roll no:'))
        self.sname = input('Enter student name:')
        self.m1 = float(input('Enter mark 1:'))
        self.m2 = float(input('Enter mark 2:'))
        return
    def computeData(self):
        self.total = self.m1 + self.m2
        self.avg = self.total / 2
        self.result = 'fail'
        if self.m1 > 34.4 and self.m2 > 34.4:
            self.result = 'pass'
            return
    def shoeData(self):
        self.computeData()
        print('Roll no:%d'%(self.rno))
        print('Student name:%s' %(self.sname))
        print('mark 1:%.2f' %(self.m1))
        print('mark 2:%.2f' %(self.m2))
        print('Total:%.2f' %(self.total))
        print('Average:%.2f' %(self.avg))
        print('Result:%s' %(self.result))
        return
obj = ExamResult()
obj.setData()
obj.shoeData()
'''
Enter mark 1:56.5
Enter mark 2:63
Roll no:1001
Student name:X5
mark 1:56.50
mark 2:63.00
Total:119.50
Average:59.75
Result:pass
'''


