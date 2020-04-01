from flask import render_template
from application import app
from application.bets.models import Bet

@app.route("/")
def index():

    bcount = Bet.bet_count()
    obcount = Bet.bet_open_count()
    cspent = Bet.bet_credits_spent()

    summary = Bet.bet_summary()

    return render_template("index.html",bcount = bcount, obcount = obcount, cspent = cspent,
                           summary = summary)
