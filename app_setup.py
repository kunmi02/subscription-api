from configure import detect_configuration_mode
from subscription import create_app
from subscription.core import db


configuration_mode = detect_configuration_mode()

application = create_app(configuration_mode)

with application.app_context():
    db.init_app(application)
    db.Model.metadata.reflect(db.engine)  # load existing DB schema
    db.create_all()
