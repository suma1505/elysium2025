from a1udf import *
from flask import Flask, request, render_template

app = Flask("Calculator")
@app.route("/", methods=["GET", "POST"])
def calcWebPage():
    fno = sno = res = 0
    if request.method == "POST":
        fno = request.form.get("numfno")
        sno = request.form.get("numsno")

        fno = uToFloat(fno)
        sno = uToFloat(sno)

        sbtn = request.form.get("sbtn")
        if sbtn == "+":
            res = fno + sno
        elif sbtn == "-":
            res = fno - sno
        elif sbtn == "x":
            res = fno * sno
        elif sbtn == "/":
            res = "%.2f" %(fno / sno)
        elif sbtn == "%":
            res = fno % sno
    return render_template('b1calc1.html', fno=fno, sno=sno, res=res)
app.run(debug=True)