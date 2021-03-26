import random
import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "codingDojo!"

@app.route('/')
def index():
    if "gold_count" not in session:
        session["gold_count"] = 0

    if "current_log" not in session:
        session["current_log"] = []

    current_log = session["current_log"]
    gold_count = session["gold_count"]

    return render_template("index.html", current_log = current_log[::-1], gold_count = gold_count)

@app.route('/process_money', methods=['POST'])
def get_gold():
    if request.form["submit_form"] == "farm":
        gold = random.randrange(10,21)
        timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        event_log= f"<p class='greentext'>Got yourself a good crop this season. You've earned {gold} gold  ({timestamp})</p>"
        session["current_log"].append(event_log)
        session.modified = True
        session["gold_count"] += gold
    if request.form["submit_form"] == "cave":
        gold = random.randrange(5,11)
        timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        event_log= f"<p class='bluetext'>You've found some treasure! Found {gold} gold  ({timestamp})</p>"
        session["current_log"].append(event_log)
        session.modified = True
        session["gold_count"] += gold
    if request.form["submit_form"] == "house":
        gold = random.randrange(2,6)
        timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        event_log= f"<p class='orangetext'>Earned {gold} gold from looting a random house! ({timestamp})</p>"
        session["current_log"].append(event_log)
        session.modified = True
        session["gold_count"] += gold
    if request.form["submit_form"] == "casino":
        gana_O_pierde = random.randrange(1,3)
        if gana_O_pierde == 1: #gana
            gold = random.randrange(0,51)
            timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            event_log= f"<p class='purpletext'>Earned {gold} gold from the casino! Fortune is with you! ({timestamp})</p>"
            session["current_log"].append(event_log)
            session.modified = True
            session["gold_count"] += gold
        else:
            gold = random.randrange(0,51) #pierde
            timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            event_log= f"<p class='redtext'>Entered a casino and lost {gold} golds... Ouch.. ({timestamp})</p>"
            session["current_log"].append(event_log)
            session.modified = True
            session["gold_count"] -= gold
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear() # borra todas las claves de la session
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)