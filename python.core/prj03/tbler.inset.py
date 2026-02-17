from mysql import connector
cn=connector.connect(host ='localhost', port=3307, database='dbsu', user='root', password='')
cr=cn.cursor()
qry1="""insert into tbler(sname, m1, m2)values('x5', 56.6, 63)"""
qry2="""insert into tbler(sname, m1, m2)values
('x3', 45.5, 52),
('x1', 36.5, 43),
('x2', 98, 20),
('x4', 61, 63.5)
"""
try:
    cr.execute(qry1)
    print("\nOne row affected")
except Exception as e:
    print("\nErr.", e)
try:
    cr.execute(qry2)
    cn.commit()
    print("\naffected rows:", cr.rowcount)
except Exception as e:
    print("\nErr.", e)
try:
    cr.close()
    cn.close()
    print("\nDisconnect MYSQL")
except Exception as e:
    print("\nErr.", e)
'''
One row affected

affected rows: 4

Disconnect MYSQL
'''
