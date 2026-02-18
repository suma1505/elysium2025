class ESA1Mdl:
    def __init__(self, eid=0, ename='', sal=0):
        self._eid=eid
        self._ename=ename
        self._sal=sal
        return
    def __del__(self):
        del self._eid, self._ename, self._sal
        del self._hra, self._da, self._pf, self._gpay, self._npay
        return
