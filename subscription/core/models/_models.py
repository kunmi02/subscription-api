from datetime import datetime

from subscription.core import db


class Subscription(db.Model):

    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    added_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def as_json(self):
        return {
            'email': self.email,
            'added_at': self.added_at.isoformat()
        }



