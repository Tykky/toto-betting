from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    email = db.Column(db.String(22), default="")
    phash = db.Column(db.String(144), default="")
    credits = db.Column(db.Float, default=0.0)

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name