from er02controller import ER2Ctrl

class ER3View(ER2Ctrl):
    def getData(self):
        print("\n Enter following input (s) for Exam Result model:")
        try:
            self._rno=input("\nRoll No. ")
            self._rno=int (self._rno)
        except Exception as e:
            print("\nInvalid roll no")
        self._sname=input("\nStudent name:")
        try:
            self._m1=input("\nMark 1. ")
            self._m1=float (self._m1)
        except Exception as e:
            print("\nInvalid mark 1")
        
        try:
            self._m2=input("\nMark 2. ")
            self._m2=float (self._m2)
        except Exception as e:
            print("\nInvalid Mark 2")
        return
    def showData(self):
        self.computeData()
        op = f"\n{self._rno:<10}"
        op += f"{self._sname:<10}"
        op += f"{self._m1:<10}"
        op += f"{self._m2:<10}"
        op += f"{self._total:<10}"
        op += f"{self._avg:<10}"
        op += f"{self._result:<10}"
        print(op)
        
obj=ER3View()
# obj.getData()
# obj.showData()
# obj.setData(1001, 'x3', 45.5, 52)
# obj.getData()
# obj.showData()

# obj.addNewRow('x5', 56.5, 63)
# obj.addNewRow('x3', 45.5, 52)
# obj.addNewRow('x1', 36.5, 43)
# obj.addNewRow('x2', 98, 20)
# obj.addNewRow('x4', 63.5, 61)

# obj.editRow(1009, 'x2', 43, 41)

obj.eraseRow(1007)

'''
Enter following input (s) for Exam Result model:

Roll No. 1001

Student name:x5

Mark 1. 56.6

Mark 2. 63

1001      x5        56.6      63.0      119.6     59.8      pass      

 Enter following input (s) for Exam Result model:

Roll No. 1002

Student name:x3

Mark 1. 45.5

Mark 2. 52

1002      x3        45.5      52.0      97.5      48.75     pass      

'''
        
'''
One row affected
'''

'''
One row affected
One row affected
One row affected
One row affected
'''

'''
One row affected
'''

'''
One row affected
'''
