from ..database import db


class Subscriber(db.Model):
    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String, nullable=False)
    subscribed = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f'<Subscriber {self.phone_number} { self.subscribed}>'
