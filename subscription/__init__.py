from flask import Flask


def _setup_blueprints(app):
    from subscription.modules.subscribers.controllers import (
        subscriber
    )
    #
    app.register_blueprint(subscriber.api_v1)


def _bind_home_url(app):
    @app.route('/')  # DEBUG
    def index():

        return 'Welcome to Email Subscribers List.'


def create_app(configuration_mode):
    from configure import load_configuration
    from subscription.core import db

    app = Flask(__name__, instance_relative_config=True)

    load_configuration(app, configuration_mode)

    _setup_blueprints(app)
    _bind_home_url(app)

    return app
