# Creating first flask app
from flask import Flask,render_template

app= Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/harry')
def harry():
    return "Hello Harry!"

app.run(debug=True)
