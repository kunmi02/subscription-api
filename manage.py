# import sys
#
# from flask_script import Manager, Shell, Server, Command  # Option
# from flask_migrate import Migrate, MigrateCommand
#
# from app_setup import db, application
#
#
# manager = Manager(application)
# migrate = Migrate(application, db)
#
#
# @manager.shell
# def _make_context():
#     return dict(app=application, db=db)
#
#
# if __name__ == '__main__':
#
#     manager.run()
