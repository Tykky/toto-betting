from application import db

class Bet(db.Model):
  
    betid = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    amount = db.Column(db.Numeric, nullable=False)
    
    userid = db.Column(db.Integer, db.ForeignKey('account.userid'), nullable=False)
    raceid = db.Column(db.Integer, db.ForeignKey('bet.betid'), nullable=False)

    def __init__(self, amount, userid, raceid):
        self.amount = amount
        self.userid = userid
        self.raceid = raceid

  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True