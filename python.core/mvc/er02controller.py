from er01model import ER1Mdl
from mysql import connector
class ER2Ctrl(ER1Mdl):
    def computeData(self):
        self._total=self._m1 + self._m2
        self._avg=self._total / 2
        self._result='pass' if (self._m1 > 34.4 and self._m2 > 34.4) else 'fail'
        return
    def setData(self, rno=0, sname='', m1=0, m2=0):
        self._rno=rno
        self._sname=sname
        self._m1=m1
        self._m2=m2
        self.computeData()
        return

    def executeQuery(self, qry):
        cn=connector.connect(host ='localhost', port=3307, database='dbsu', user='root', password='')
        cr=cn.cursor()
        try:
            cr.execute(qry)
            cn.commit()
            print("\nOne row affected")
        except Exception as e:
            print("\nErr.", e)

        try:
            cr.close()
            cn.close()
        except Exception as e:
            print("\nErr.", e)
        return        

    def addNewRow(self, sname, m1, m2):
        self._sname=sname
        self._m1=m1
        self._m2=m2
        qry=f"insert into tbler(sname, m1, m2)values('{self._sname}', {self._m1}, {self._m2})"
        self.executeQuery(qry)
        return

    def editRow(self, rno, sname, m1, m2):
        self._rno=rno
        self._sname=sname
        self._m1=m1
        self._m2=m2
        qry=f"update tbler set sname='{self._sname}', m1={self._m1}, m2={self._m2} where rno={self._rno}"
        self.executeQuery(qry)
        return

    def eraseRow(self, rno):
        self._rno=rno
        qry=f"delete from tbler where rno={self._rno}"
        self.executeQuery(qry)
        return
