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
    editData = {"1001": {"m2": "72"}, "drink/categories":{"soft": "grapes, cherry, orange juices"}}
    db.update(editData)
    print("Updated two row")
except Exception as e:
    print("Err.", e)
'''
Updated two row
'''
