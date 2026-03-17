import pyrebase
fbConfig = {
    "apiKey": "AIzaSyAgkHNtFZaGgzb2vOIQsAsfwq0rizaPkwU",
    "authDomain": "fbprj1a-e3931.firebaseapp.com",
    "databaseURL": "https://fbprj1a-e3931-default-rtdb.firebaseio.com",
  "projectId": "fbprj1a-e3931",
  "storageBucket": "fbprj1a-e3931.firebasestorage.app",
  "messagingSenderId": "515148740856",
  "appId": "1:515148740856:web:7859f9485892594822630d"
}
try:
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    rows = db.get()
    for r in rows.each():
        print(r.key(), r.val())
except Exception as e:
    print("Err.", e)
'''
1001 {'m1': '56.5', 'm2': '63', 'sname': 'x5'}
1002 {'m1': '36.5', 'm2': '43', 'sname': 'x3'}
1003 {'m1': '45.5', 'm2': '52', 'sname': 'x1'}
1004 {'m1': '98', 'm2': '20', 'sname': 'x2'}
1005 {'m1': '61', 'm2': '45.5', 'sname': 'x4'}
drink {'categories': {'soft': 'grapes, cherry, orange juices'}}
'''