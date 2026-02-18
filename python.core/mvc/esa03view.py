from esa02controller import ESA2Ctrl
class ESA3View(ESA2Ctrl):
    def getData(self):
        print("\nEnter following input (s) for Employee Salary Allowance model:")
        try:
            self._eid=input("\nEid.")
            self._eid=int(self._eid)
        except Exception as e:
            print("\n Invalid eid")
        self._ename=input("\nEmployee name:")
        try:
            self._sal=input("\nSalary.")
            self._sal=double(self._sal)
        except Exception as e:
            print("\nInvalid salary")
            return
        def showData(self):
            self.compute()
            op=f"\n{self._eid:<10}"
            op+=f"{self._ename:<10}"
            op+=f"{self._sal:<10}"
            op+=f"{self._hra:<10}"
            op+=f"{self._da<10}"
            op+=f"{self._pf:<10}"
            op+=f"{self._npay:<10}"
            op+=f"{self._gpay:<10}"
            print(op)
obj=ESA3View()
#obj.addNewRow('x5', 500000)
#obj.addNewRow('x3', 300000)
#obj.addNewRow('x1', 100000)
#obj.addNewRow('x2', 200000)
#obj.addNewRow('x4', 400000)

#obj.editRow(1004, 'x2',100000)

obj.eraseRow(1004)

'''
One row affected
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



