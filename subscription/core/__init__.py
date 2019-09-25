from flask_sqlalchemy import SQLAlchemy

from .query_middleware import CustomQuery


db = SQLAlchemy(query_class=CustomQuery)

