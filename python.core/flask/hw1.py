from flask import Flask
app=Flask("Hello World")
@app.route("/", methods=["GET","POST"])
def homePage():
    return "<h1>Hello World!</h1>"
app.run(debug=True)
