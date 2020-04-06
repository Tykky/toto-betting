from application import db

class Horse(db.Model):
  
    horseid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False, unique=True)
    breed = db.Column(db.String(16), nullable=False)
    tier = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(2000), nullable=False)

    def __init__(self, name, breed, tier, description):
        self.name = name
        self.breed = breed
        self.tier = tier
        self.description = description

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return False