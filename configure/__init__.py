# -*- coding: utf-8 -*-
"""
    config
    ----------------------
    A module providing all configuration for the application.
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SECRET_KEY = 'your-super-secret-key'
    LOG_REQUESTS = True
    USE_DUMMY_GATEWAY_RESPONSES = False

    # pagination
    PAGINATION_DEFAULT_PAGE = 1
    PAGINATION_DEFAULT_PER_PAGE = 20

    DEFAULT_REQUESTS_TIMEOUT = 11.0  # seconds


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class PilotConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True

    # CELERY_CONFIG = {'CELERY_ALWAYS_EAGER': True}
    WTF_CSRF_ENABLED = False

    # SQLALCHEMY_DATABASE_URI = "sqlite:///subscription_db"
    SQLALCHEMY_DATABASE_URI = "sqlite://"  # in-memory database


config_modes = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'pilot': PilotConfig,
    'production': ProductionConfig
}


def detect_configuration_mode():
    from subscription.core.constants import ALLOWED_CONFIGURATION_MODES
    from subscription.core.errors import ConfigNotFound

    config_mode = os.environ['RUNNING_MODE']
    if config_mode in ALLOWED_CONFIGURATION_MODES:
        print '"%s" configuration mode detected.' % config_mode
        return config_mode

    error_message = ('Invalid or no configuration mode ("{0}") detected! '
                     'Aborting...'.format(config_mode))
    raise ConfigNotFound(error_message)


def load_configuration(app, mode):
    """
    Load the applicable configuration for the application
    :param app: the application
    :param mode: the mode signalling which configuration object to load
    :return: None
    """

    configuration = config_modes[mode]
    app.config.from_object(configuration)  # Load pre-defined by class/object

    # Load from environment
    instance_config = {
        True: 'config.py',
        False: 'test_config.py'
    }[configuration != TestConfig]
    app.config.from_pyfile(instance_config, silent=True)


