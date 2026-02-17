class ER1Mdl:
    def __init__(self, rno=0, sname='', m1=0.0, m2=0.0):
        self.__rno=rno
        self.__sname=sname
        self.__m1=m1
        self.__m2=m2
        self.__total=self.__m1 + self.__m2
        self.__avg=self.__total / 2
        self.__result='pass' if self.__m1 > 34.4 and self.__m2 > 34.4 else 'fail'
        return
    def __del__(self):
        del self.__rno, self.__sname, self.__m1, self.__m2
        del self.__total, self.__avg, self.__result
        return
    def getData(self):
        op = f"{self.__rno:<10}"
        op += f"{self.__sname:<10}"
        op += f"{self.__m1:<10}"
        op += f"{self.__m2:<10}"
        op += f"{self.__total:<10}"
        op += f"{self.__avg:<10}"
        op += f"{self.__result:<10}"
        return op
'''    
obj=ER1Mdl()
print(obj)
print(obj.getData())

obj=ER1Mdl(1001, 'x5', 56.5, 63)
print(obj)
print(obj.getData())

print(ER1Mdl(1002, 'x3', 45.5, 52).getData())
'''
'''
<__main__.ER1Mdl object at 0x000002A765652A50>
0                   0.0       0.0       0.0       0.0       fail      
<__main__.ER1Mdl object at 0x000002A765657C50>
1001      x5        56.5      63        119.5     59.75     pass      
1002      x3        45.5      52        97.5      48.75     pass      
'''
    
