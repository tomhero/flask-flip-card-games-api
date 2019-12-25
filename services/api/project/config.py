import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MONGO_DATABASE_HOST = os.getenv("DATABASE_HOSTNAME", "flipcardcluster0-ngcow.mongodb.net/test?retryWrites=true&w=majority")
    MONGO_DATABASE_USER = os.getenv("DATABASE_USERNAME", "flaskuser")
    MONGO_DATABASE_PASS = os.getenv("DATABASE_PASSWORD", "9K2fmXThIrKYuo1x")