# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import birthday_countdown1


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result', methods = ["GET", "POST"])
def timeleft():

    input1 = request.form["month1"]
    input2 = request.form["month2"]
    input1_int = birthday_countdown1(input1)
    input2_int = birthday_countdown1(input2)    
    message = abs(input1_int - input2_int)
    
    
    return render_template("timeleft.html", message = message)
#return redirect("/index")

# @app.route('/result', methods = ["GET", "POST"])
# def timeleft():
#     input1 = request.form["month1"]
#     input2 = request.form["month2"]
#     input1_int = birthday_countdown1(input1)
#     input2_int = birthday_countdown1(input2)    
#     message = abs(input1_int - input2_int)
    
    
#     return render_template("timeleft.html", message = message)
