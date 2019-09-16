# # -*- coding: utf-8 -*-
# """
#     config
#     ----------------------
#     A module providing all configuration for the application.
# """
# import os
#
#
# basedir = os.path.abspath(os.path.dirname(__file__))
#
#
# class BaseConfig(object):
#     SECRET_KEY = 'your-super-secret-key'
#     LOG_REQUESTS = True
#     USE_DUMMY_GATEWAY_RESPONSES = False
#
#     # pagination
#     PAGINATION_DEFAULT_PAGE = 1
#     PAGINATION_DEFAULT_PER_PAGE = 20
#
#     AUTH_REQUIREMENT_ENABLED = True
#     CHECKSUM_REQUIREMENT_ENABLED = True
#
#     DEFAULT_REQUESTS_TIMEOUT = 11.0  # seconds
#
#     RECEIPT_LENGTH = 17
#
#     # http://flask-sqlalchemy.pocoo.org/2.1/config/
#     # SQLALCHEMY_RECORD_QUERIES = True
#
#     # SQLALCHEMY_POOL_SIZE = 20  # set to 0 to get unlimited open connections
#     # SQLALCHEMY_MAX_OVERFLOW = 23  # set to -1 to indicate no overflow limit
#
#     # number of seconds to wait before giving up on getting a connection from
#     # the pool
#     # SQLALCHEMY_POOL_TIMEOUT = 20
#
#     # recycle connections after the given number of seconds has passed:
#     # -1 == no timeout
#     # SQLALCHEMY_POOL_RECYCLE = -1
#
#     # SQLALCHEMY_ECHO = True
#     # SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#
#     # change this to True if the site is being maintained
#     # MAINTENANCE_MODE = False
#
#     CELERY_INCLUDE = ['tasks']
#
#     SENTRY_CONTEXT = {
#         'api_ref': {
#             'name': 'api_ref',
#             'attr': 'api_ref',
#             'default': 'NO API-REF'
#         }
#     }
#
#     SENTRY_USER_CONTEXT = {
#         'user_category': {
#             'name': 'user_category',
#             'attr': 'user.user_category.name',
#             'default': 'NO USER CATEGORY'
#         },
#         'username': {
#             'name': 'username',
#             'attr': 'user.username',
#             'default': 'NO USERNAME'
#         },
#         'email': {
#             'name': 'email',
#             'attr': 'user.email',
#             'default': 'NO EMAIL'
#         },
#         'phone': {
#             'name': 'phone',
#             'attr': 'user.phone',
#             'default': 'NO PHONE'
#         },
#         'address': {
#             'name': 'address',
#             'attr': 'user.address',
#             'default': 'NO ADDRESS'
#         },
#         'first_name': {
#             'name': 'first_name',
#             'attr': 'user.first_name',
#             'default': 'NO FIRST NAME'
#         },
#         'last_name': {
#             'name': 'last_name',
#             'attr': 'user.last_name',
#             'default': 'NO LAST NAME'
#         }
#     }
#
#     REQUESTS_LOGGING_EXEMPTED_ENDPOINTS = []
#     LOG_FILTERED_KEYWORDS = ['password', 'Authorization', 'X-Api-Key']
#
#
# class DevelopmentConfig(BaseConfig):
#     DEBUG = True
#     TESTING = False
#
#     # AUTH_REQUIREMENT_ENABLED = False
#     CHECKSUM_REQUIREMENT_ENABLED = False
#
#
# class PilotConfig(BaseConfig):
#     DEBUG = False
#     TESTING = False
#
#
# class ProductionConfig(BaseConfig):
#     DEBUG = False
#     TESTING = False
#
#
# class TestConfig(BaseConfig):
#     DEBUG = False
#     TESTING = True
#
#     # CELERY_CONFIG = {'CELERY_ALWAYS_EAGER': True}
#     WTF_CSRF_ENABLED = False
#
#     # SQLALCHEMY_DATABASE_URI = "sqlite:///tacore_db"
#     SQLALCHEMY_DATABASE_URI = "sqlite://"  # in-memory database
#     # SQLALCHEMY_ECHO = True
#
#
# config_modes = {
#     'development': DevelopmentConfig,
#     'testing': TestConfig,
#     'pilot': PilotConfig,
#     'production': ProductionConfig
# }
#
#
# def detect_configuration_mode():
#     from subscription.core.constants import ALLOWED_CONFIGURATION_MODES
#     from subscription.core.errors import ConfigNotFound
#
#     config_mode = os.environ['RUNNING_MODE']
#     if config_mode in ALLOWED_CONFIGURATION_MODES:
#         print '"%s" configuration mode detected.' % config_mode
#         return config_mode
#
#     error_message = ('Invalid or no configuration mode ("{0}") detected! '
#                      'Aborting...'.format(config_mode))
#     raise ConfigNotFound(error_message)
#
#
# def load_configuration(app, mode):
#     """
#     Load the applicable configuration for the application
#     :param app: the application
#     :param mode: the mode signalling which configuration object to load
#     :return: None
#     """
#     from subscription.core import logger
#
#     configuration = config_modes[mode]
#     app.config.from_object(configuration)  # Load pre-defined by class/object
#
#     # Load from environment
#     instance_config = {
#         True: 'config.py',
#         False: 'test_config.py'
#     }[configuration != TestConfig]
#     app.config.from_pyfile(instance_config, silent=True)
#
#     if app.config['RECEIPT_LENGTH'] < 17:
#         raise ValueError('Receipt length cannot be less than 17.')
#
#     if app.config['USE_DUMMY_GATEWAY_RESPONSES']:
#         logger.warn('****DUMMY GATEWAY API RESPONSES TURNED ON!!! '
#                     'NOT SAFE FOR PRODUCTION!****')
