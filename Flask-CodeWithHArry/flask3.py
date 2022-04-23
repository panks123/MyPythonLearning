# jinja templating

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def fun():
    name="Pankaj Kumar"
    return render_template('jinja_templating.html',name=name)

app.run(debug=True)