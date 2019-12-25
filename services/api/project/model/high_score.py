import datetime
from bson.objectid import ObjectId
"""
High Score Class should handle new highscore from player
then put the timestamp before save to database
"""


class HighScore:

    __collection__ = "high_score"

    def __init__(self, db):
        self.db = db

    def get_high_scores(self):
        _scores = self.db[self.__collection__].find()

        data = []
        item = {}

        for score in _scores:
            item = {
                "id": str(score["_id"]),
                "highscore": score["high_score"],
                "achievedAt": score["achieved_date"]
            }
            data.append(item)
        return data

    def get_the_highest_score(self):
        data = {
            "globalHighscore": None,
            "achievedAt": None
        }
        raw_result = self.db[self.__collection__].find_one({"high_score": {"$exists": True}}, sort=[("high_score", 1)])
        if raw_result is not None:
            data = {
                "id": str(raw_result["_id"]),
                "globalHighscore": raw_result["high_score"],
                "achievedAt": raw_result["achieved_date"]
            }
        return data

    def get_highscore_by_id(self, id):
        raw_result = self.db[self.__collection__].find_one({"_id": ObjectId(id)})
        data = {
            "highscore": None,
            "achievedAt": None
        }
        if raw_result is not None:
            data = {
                "id": str(raw_result["_id"]),
                "highscore": raw_result["high_score"],
                "achievedAt": raw_result["achieved_date"]
            }
        return data

    def insert_new_high_score(self, new_score):
        item = {
            "achieved_date": datetime.datetime.utcnow(),
            "high_score": new_score
        }
        return self.db[self.__collection__].insert_one(item)
