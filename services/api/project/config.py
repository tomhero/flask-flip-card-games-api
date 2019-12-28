import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    PYMONGO_DATABASE_URI = os.getenv("DATABASE_URL", "mongodb://")
    MONGO_DATABASE_NAME = os.getenv("DATABASE_NAME")
    FLASK_API_KEY = os.getenv("API_KEY", "sdf3sdc3s4s654y5h633554g1ds6dfg1sd8d4f6")
