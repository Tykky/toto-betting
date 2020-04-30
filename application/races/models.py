from application import db


class Race(db.Model):

    raceid = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    name = db.Column(db.String(16), nullable=False)
    location = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(2000))

    isopen = db.Column(db.Boolean, nullable=False)

    horses = db.relationship("Horse", secondary='connector')

    def __init__(self, name, location, description=""):
        self.name = name
        self.location = location
        self.description = description
        self.isopen = False

    def get_id(self):
        return self.raceid

    def is_active(self):
        return True 

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return False

class Connector(db.Model):

    horseid = db.Column(db.Integer, db.ForeignKey('horse.horseid'), primary_key=True)
    raceid = db.Column(db.Integer, db.ForeignKey('race.raceid'), primary_key=True)

    def __init__(self, raceid, horseid):
        self.raceid = raceid
        self.horseid = horseid

    def get_id(self):
        return self.raceid

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return False