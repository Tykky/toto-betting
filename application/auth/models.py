from application import db

class User(db.Model):

    __tablename__ = "account"
  
    userid = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(12), nullable=False, unique=True)
    phash = db.Column(db.Binary(60), nullable=False)
    credits = db.Column(db.Float, nullable=False)
    isadmin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, phash):
        self.username = username
        self.phash = phash
        self.credits = 0.0
        self.isadmin = False
  
    def get_id(self):
        return self.userid

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.isadmin:
            return["ADMIN","USER"]
        else:
            return["USER"]

