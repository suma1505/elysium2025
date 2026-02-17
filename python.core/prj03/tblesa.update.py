from mysql import connector
class CtrlESA:
    def __init__(self):
        try:
            self.cn = connector.connect(host ="127.0.0.1", port = 3307, user = "root", password = "", database = "dbsu")
            self.cr = self.cn.cursor()
        except Exception as e:
            print("Err:", e)
        return
    def editRow(self, eid, sal):
        qry = f"update tblesa set sal = {sal} where eid = {eid}"
        try:
            self.cr.execute(qry)
            print("affected 1 row")
        except Exception as e:
            print("err:", e)
            return
obj = CtrlESA()
obj.editRow(1006, 700000)

