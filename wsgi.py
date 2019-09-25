import os

from app_setup import application


os.environ['FLASK_ENV'] = 'development' if application.debug else 'production'


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=1234)

