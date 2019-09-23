from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Subscription(db.Model):

    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_address = db.Column(db.String(50), unique=True)
    added_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def as_json(self):
        return {
            'Email': self.email_address,
            'added_at': self.added_at.isoformat()
        }



