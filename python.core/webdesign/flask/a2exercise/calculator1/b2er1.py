from a1udf import *
from flask import Flask, render_template, request
app = Flask("b2ExamResult")
@app.route('/', methods=["GET", "POST"])
def erWebPage():
    rno = sname = m1 = m2 = total = avg = result =''
    if request.method == "POST":
        rno = request.form.get('numrno')
        sname = request.form.get('tbxsname')
        m1 = request.form.get('numm1')
        m2 = request.form.get('numm2')
        rno = uToInt(rno)
        m1 = uToFloat(m1)
        m2 = uToFloat(m2)
        total = m1 + m2
        avg = total / 2
        result = 'pass' if m1 > 34.4 and m2 > 34.4 else 'fail'

    res = {
        'rno': rno,
        'sname': sname,
        'm1': m1,
        'm2': m2,
        'total': total,
        'avg': avg,
        'result': result
    }
    return render_template('b2er1.html', **res)
app.run(debug=True)
