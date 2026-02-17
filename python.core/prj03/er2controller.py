from er1model import ER1Mdl

class ER2Ctrl(ER1Mdl):
    def __init__(self, rno=0, sname='', m1=0.0, m2=0.0):
        super().__init__(rno, sname, m1, m2)
        return
obj =ER2Ctrl()
print(obj.getData())

obj=ER2Ctrl(1001, 'x5', 56.5, 63)
print(obj.getData())

print(ER2Ctrl(1002, 'x3', 45.5, 52).getData())

'''
0                   0.0       0.0       0.0       0.0       fail      
1001      x5        56.5      63        119.5     59.75     pass      
1002      x3        45.5      52        97.5      48.75     pass      
'''
