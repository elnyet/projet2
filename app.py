from flask import Flask, render_template, request, url_for
from apps.money import *

app = Flask(__name__)

@app.get("/money")
def money_form():
    if request.args.get('money') != None :
        money = float(request.args.get('money'))
    else:
        money = 1
    
    money = rendre_somme(money)

    return render_template('money.html', money=money)