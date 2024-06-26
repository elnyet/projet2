from flask import Flask, render_template, request, url_for
from apps.money import *
from apps.bag import *

app = Flask(__name__)

@app.get("/money")
def money_form():
    # check si l'utilisateur a r mis
    if request.args.get('money') != None :
        money = float(request.args.get('money'))
    else:
        money = 1
    
    money = rendre_somme(money)

    return render_template('money.html', money=money)

@app.route("/bag", methods=['GET', 'POST'])
def bag_form():
    if request.method == 'POST':
        items=[
                {"weight":float(request.form['weight_item1']),"price":float(request.form['price_item1'])},
                {"weight":float(request.form['weight_item2']),"price":float(request.form['price_item2'])},
                {"weight":float(request.form['weight_item3']),"price":float(request.form['price_item3'])},
                {"weight":float(request.form['weight_item4']),"price":float(request.form['price_item4'])},
        ]
        
        baglimit=float(request.form['baglimit'])

        sorted_price=sort_by_price(items)
        result_price=greedy_kp(sorted_price, baglimit)

        sorted_weight=sort_by_weight(items)
        result_weight=greedy_kp(sorted_weight, baglimit)

        sorted_ratio=sort_by_ratio(items)
        result_ratio=greedy_kp(sorted_ratio, baglimit)

        return render_template('bag.html', result_price=result_price, result_weight=result_weight, result_ratio=result_ratio)

    return render_template('bag.html')
