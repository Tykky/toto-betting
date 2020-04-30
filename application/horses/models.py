from application import db

class Horse(db.Model):
  
    horseid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False, unique=True)
    breed = db.Column(db.String(16), nullable=False)
    tier = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    wins = db.Column(db.Integer, nullable=False)

    races = db.relationship("Race", secondary='connector')
    bets = db.relationship("Bet", backref='horse', lazy=True)

    def __init__(self, name, breed, tier, description):
        self.name = name
        self.breed = breed
        self.tier = tier
        self.description = description
        self.wins = 0

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return False

    def contains_raceid(self, raceid):
        for race in self.races:
            if race.raceid == raceid:
                return True
        return False