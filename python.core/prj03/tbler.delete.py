from mysql import connector
cn=connector.connect(host ='localhost', port=3307, database='dbsu', user='root', password='')
cr=cn.cursor()
qry1="""delete from tbler where rno=1003"""
qry2="""delete from tbler"""
try:
    cr.execute(qry1)
    cn.commit()
    print("\nErased one row")
except Exception as e:
    print("\nErr.", e)
try:
    cr.execute(qry2)
    cn.commit()
    print("\nErased", cr.rowcount,'roe(s)')
except Exception as e:
    print("\nErr.", e)
try:
    cr.close()
    cn.close()
    print("\nDisconnect MYSQL")
except Exception as e:
    print("\nErr.", e)

'''
Erased one row

Erased 4 roe(s)

Disconnect MYSQL
'''
