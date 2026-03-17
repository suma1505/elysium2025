import pyrebase
rows = [
    {"sname": "x5", "m1":"56.5", "m2":"63"},
    {"sname": "x3", "m1":"36.5", "m2":"43"},
    {"sname": "x1", "m1":"45.5", "m2":"52"},
    {"sname": "x2", "m1":"98", "m2":"20"},
    {"sname": "x4", "m1":"61", "m2":"45.5"}

]
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
    rno = 1001
    fb = pyrebase.initialize_app(fbConfig)
    db = fb.database()
    for row in rows:
        db.child(str(rno)).set(row)
        rno += 1
    print("Added five row(s)")
except Exception as e:
    print("Err.", e)
'''
Added five row(s)
'''