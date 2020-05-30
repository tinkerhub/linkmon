import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

class Config(object):
    HOST = os.environ.get('HOST')
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    DEBUG=False

class StagingConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class StagingConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class TestingConfig(Config):
    TESTING=True
    DEBUG=True