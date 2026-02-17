class ER1Mdl:
    def __init__(self, rno=0, sname='', m1=0.0, m2=0.0):
        self._rno=rno
        self._sname=sname
        self._m1=m1
        self._m2=m2
        return

    def __del__(self):
        del self._rno, self._sname, self._m1, self._m2
        del self._total, self._avg, self._result
        return
