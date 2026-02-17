from mysql import connector
cn=connector.connect(host ='localhost', port=3307, database='dbsu', user='root', password='')
cr=cn.cursor()
qry1="""update tbler set m1=59, m2=70 where result='fail'"""
qry2="""update tbler set m2=m2+5"""
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

affected rows: 5

Disconnect MYSQL
'''
