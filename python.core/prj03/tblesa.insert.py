from mysql import connector
class CtrlESA:
    def __init__(self):
        try:
            self.cn = connector.connect(host ="127.0.0.1", port = 3307, user = "root", password = "", database = "dbsu")
            self.cr = self.cn.cursor()
        except Exception as e:
            print("Err:", e)
        return
    def addNewRow(self, ename, sal):
        qry = f"insert into tblesa (ename, sal) values ('{ename}', {sal})"
        try:
            self.cr.execute(qry)
            print("affected 1 row")
        except Exception as e:
            print("err:", e)
            return
obj = CtrlESA()
obj.addNewRow('t5', 500000)

