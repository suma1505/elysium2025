from a1udf import *
from flask import Flask, render_template, request
app = Flask("b4Electricity Bill")
@app.route('/', methods=['GET','POST'])
def estWebPage():
    eid = ename = sal = tax10 = tax20 = tax30 = tottax = npay = ''
    if request.method == "POST":
        eid = request.form.get('numeid')
        ename = request.form.get('tbxename')
        sal = request.form.get('numsal')

        eid = uToInt(eid)
        sal = uToFloat(sal)
        if (sal > 1000000):
            tax10 = 250000 * 10/100
            tax20 = 500000 * 20/100
            tax30 = (sal - 1000000) * 30/100
        elif (sal > 500000):
            tax10 = 250000 * 10/100
            tax20 = (sal - 500000) * 20/100
        elif (sal > 250000):
            tax10 = (sal - 250000) * 10/100

        tottax= tax10 + tax20 + tax30
        npay = sal - tottax

    res = {
        'eid': eid,
        'ename': ename,
        'sal': sal,
        'tax10': tax10,
        'tax20': tax20,
        'tax30': tax30,
        'tottax': tottax,
        'npay': npay,
    }
    return render_template('b4est1.html', **res)
app.run(debug=True)
