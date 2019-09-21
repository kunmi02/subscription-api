from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Subscriber(db.Model):
    """
    Create a Subscriber table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'subscribers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_address = db.Column(db.String(50), unique=True)
    added_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, email_address):
        self.email_address = email_address

    def as_json(self):
        return {
            'id': self.id,
            'Email': self.email_address,
            'added_at': self.added_at
        }



