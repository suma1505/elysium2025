from mysql import connector
from esa01model import ESA1Mdl
class ESA2Ctrl(ESA1Mdl):
    def computeData(self):
        self._hra=self._sal * 20/100
        self._da=self._sal * 15/100
        self._pf=self._sal *35/100
        self._gpay=self._sal + sel._hra + self._da
        self._npay=self._gpay - self._pf
        return
    def setData(self, eid=0, ename='', sal=0):
        self._eid=eid
        self._ename=ename
        self._sal=sal
        self.computeData()
        return
    def executeQuery(self, qry):
        cn=connector.connect(host='localhost', port=3307, database='dbsu', user='root', password='')
        cr=cn.cursor()
        try:
            cr.execute(qry)
            cn.commit()
            print("\nOne row affected")
        except Exception as e:
            print("\nErr.:", e)
        try:
            cr.cloise()
            cn.close()
        except Exception as e:
            print("\nErr.:")
            return
    def addNewRow(self, ename, sal):
        self._ename=ename
        self._sal=sal
        qry=f"insert into tblesa (ename, sal)values('{self._ename}', {self._sal})"
        self.executeQuery(qry)
        return
    def editRow(self, eid, ename, sal):
        self._eid=eid
        self._ename=ename
        self._sal=sal
        qry=f"update tblesa set ename='{self._ename}', sal={self._sal} where eid={self._eid}"
        self.executeQuery(qry)
        return
    def eraseRow(self, eid):
        self._eid=eid
        qry=f"delete from tblesa where eid={self._eid}"
        self.executeQuery(qry)
        return
   
        
        
