from marketing_notifications_python.models import app_db

db = app_db()


class Subscriber(db.Model):
    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String, nullable=False)
    subscribed = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<Subscriber %r %r>' % self.phone_number, self.subscribed
