import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    PYMONGO_DATABASE_URI = os.getenv("DATABASE_URL", "mongodb://")
    MONGO_DATABASE_NAME = os.getenv("DATABASE_NAME")