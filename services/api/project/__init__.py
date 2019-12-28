from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_talisman import Talisman
import flask_monitoringdashboard as dashboard
from pymongo import MongoClient
from project.model.high_score import HighScore

app = Flask(__name__)
CORS(app)
Talisman(app)
dashboard.bind(app)
app.config.from_object("project.config.Config")

client = MongoClient(app.config["PYMONGO_DATABASE_URI"])
db = client[app.config["MONGO_DATABASE_NAME"]]

high_score_model = HighScore(db)
api_key = app.config["FLASK_API_KEY"]


@app.route("/")
def index():
    return jsonify(
        status=True,
        message="Welcome to the Dockerized Flask MongoDB app!"
    )


@app.route("/api/v1/highscores/<client_api_key>")
def get_all_score(client_api_key):
    if (not validate_api_key(api_key)):
        return jsonify(status=False), 400
    all_score = high_score_model.get_high_scores()
    return jsonify(
        status=True,
        scores=all_score
    )


@app.route("/api/v1/highscore/<client_api_key>")
def get_only_highest_score(client_api_key):
    if (not validate_api_key(api_key)):
        return jsonify(status=False), 400
    score = high_score_model.get_the_highest_score()
    score["status"] = True
    return jsonify(score)


@app.route("/api/v1/highscore/<client_api_key>", methods=["POST"])
def add_new_high_score(client_api_key):
    if (not validate_api_key(api_key)):
        return jsonify(status=False), 400
    request_data = request.get_json(force=True)

    current_global_highscore = high_score_model.get_the_highest_score()

    # NOTE : playerHighscore will be inserted when is the new player's highscore
    insert_result = high_score_model.insert_new_high_score(request_data["playerHighscore"])
    inserted_player_highscore = high_score_model.get_highscore_by_id(insert_result.inserted_id)

    is_break_the_record = False
    if current_global_highscore["globalHighscore"] is None or request_data["playerHighscore"] < current_global_highscore["globalHighscore"]:
        # NOTE : When player breaks the record!!
        is_break_the_record = True
        current_global_highscore["globalHighscore"] = request_data["playerHighscore"]
        current_global_highscore["achievedAt"] = inserted_player_highscore["achievedAt"]

    return jsonify(
        status=True,
        isBreakTheRecord=is_break_the_record,
        globalHighscore=current_global_highscore["globalHighscore"],
        globalAchievedAt=current_global_highscore["achievedAt"],
        playerAchievedAt=inserted_player_highscore["achievedAt"],
        message="New highscore from player saved successfully!"
    ), 201


def validate_api_key(key):
    return key == api_key
