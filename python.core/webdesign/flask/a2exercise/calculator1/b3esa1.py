from a1udf import *
from flask import Flask, render_template, request
app = Flask("b3Employee Salary Allowance")
@app.route('/', methods=['GET','POST'])
def esaWebPage():
    eid = ename = sal = hra = da = pf = gpay = npay = ''
    if request.method == "POST":
        eid = request.form.get('numeid')
        ename = request.form.get('tbxename')
        sal = request.form.get('numsal')

        eid = uToInt(eid)
        sal = uToFloat(sal)


        hra = sal * 20/100
        da = sal * 15/100
        pf = sal * 35/100
        gpay = sal + hra + da
        npay = gpay - pf
        print(npay)

    res = {
        'eid': eid,
        'ename': ename,
        'sal': sal,
        'hra': hra,
        'da': da,
        'pf': pf,
        'gpay': gpay,
        'npay': npay,
    }
    return render_template('b3esa1.html', **res)
app.run(debug=True)
