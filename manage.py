from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

from app_setup import application
from subscription.core.models import db

manager = Manager(application)
migrate = Migrate(application, db)


@manager.shell
def _make_context():
    return dict(app=application, db=db)


manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()

