class ERMdl:
    def computeData(self):
        self.__total=self.m1 + self.m2
        self.__avg=self.__total / 2
        self.__result='pass' if (self.m1 > 34.4 and self.m2 > 34.4) else 'fail'
        return
    def setData(self, rno=0, sname=None, m1=0, m2=0):
        self.rno=rno
        self.sname=sname
        self.m1=m1
        self.m2=m2
        self.__total=0.0
        self.__avg=0.0
        self.__result='fail'
        return
    def getData(self):
        print("\n Enter following input(s) for exam result model:")
        try:
            self.rno=input("\nRoll No.: ")
            self.rno=int (self.rno)
        except Exception as e:
            print("\n invalid rool no")
        self.sname=input("\nStudent Name: ")
        try:
            self.m1=input("\n Mark 1: ")
            self.m1=float (self.m2)
        except Exception as e:
            print("\n invalid mark 1 ")
        try:
            self.m1=input("\n Mark 2: ")
            self.m1=float (self.m2)
        except Exception as e:
            print("\n invalid mark 2 ")
        self.computeData()
        return
    def __init__(self, rno=0, sname=None, m1=0.0, m2=0.0):
        self.setData(rno, sname, m1, m2)
        return
    def __del__(self):
        del self.rno, self.sname, self.m1, self.m2
        del self.__total, self.__avg, self.__result
        print("\n Erased all instance variable from memory")
        return
    def __str__(self):
        self.computeData()
        op=f"\n{self.rno:<10}"
        op+=f"{self.sname:<10}"
        op+=f"{self.m1:<10}"
        op+=f"{self.m2:<10}"
        op+=f"{self.__total:<10}"
        op+=f"{self.__avg:<10}"
        op+=f"{self.__result:<10}"
        return op
obj=ERMdl(1001, 'x5', 98, 20)
print(obj)

obj.setData(1001, 'x5', 56.5, 63)
print(obj)

obj.getData()
print(obj)

del obj

'''
1001      x5        98        20        118       59.0      fail      

1001      x5        56.5      63        119.5     59.75     pass      

 Enter following input(s) for exam result model:

Roll No.: 1002

Student Name: x3

 Mark 1: 45.5

 Mark 2: 52

1002      x3        63.0      63        126.0     63.0      pass      

 Erased all instance variable from memory
'''
