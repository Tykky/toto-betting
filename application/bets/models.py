from application import db
from sqlalchemy.sql import text

class Bet(db.Model):
  
    betid = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    amount = db.Column(db.Numeric, nullable=False)
    
    isopen = db.Column(db.Boolean, nullable=False)

    userid = db.Column(db.Integer, db.ForeignKey('account.userid'), nullable=False)
    raceid = db.Column(db.Integer, db.ForeignKey('race.raceid'), nullable=False)
    horseid = db.Column(db.Integer, db.ForeignKey('horse.horseid'), nullable=False)

    def __init__(self, amount, userid, raceid, horseid):
        self.amount = amount
        self.userid = userid
        self.raceid = raceid
        self.isopen = True
        self.horseid = horseid

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return False

    @staticmethod
    def bet_count():
        stmt = text("SELECT COUNT(bet.betid) FROM bet")
        return db.engine.execute(stmt).first()[0]

    @staticmethod
    def bet_open_count():
        stmt = text("SELECT COUNT(bet.betid) FROM bet"
                    " INNER JOIN race ON race.raceid = bet.raceid"
                    " WHERE race.isopen IS TRUE")
        return db.engine.execute(stmt).first()[0]

    @staticmethod
    def bet_credits_spent():
        stmt = text("SELECT SUM(bet.amount) FROM bet")
        return db.engine.execute(stmt).first()[0]

    @staticmethod
    def bet_summary():
        stmt = text("SELECT account.username, race.name, race.location, bet.amount"
                    " FROM bet INNER JOIN race ON race.raceid = bet.raceid"
                    " INNER JOIN account ON account.userid = bet.userid"
                    " WHERE race.isopen IS TRUE")
        return db.engine.execute(stmt)