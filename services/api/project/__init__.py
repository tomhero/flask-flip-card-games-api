from flask import Flask, jsonify, request
from pymongo import MongoClient
from project.model.high_score import HighScore

app = Flask(__name__)
app.config.from_object("project.config.Config")

client = MongoClient(f"mongodb+srv://{app.config['MONGO_DATABASE_USER']}:{app.config['MONGO_DATABASE_PASS']}@{app.config['MONGO_DATABASE_HOST']}")
db = client.flipcard

high_score_model = HighScore(db)

@app.route("/")
def index():
    return jsonify(
        status=True,
        message="Welcome to the Dockerized Flask MongoDB app!"
    )

@app.route("/api/v1/highscores")
def get_all_score():
    all_score = high_score_model.get_high_scores()
    return jsonify(
        scores=all_score
    )

@app.route("/api/v1/highscore")
def get_only_highest_score():
    score = high_score_model.get_the_highest_score()
    return jsonify(score)

@app.route("/api/v1/highscore", methods=["POST"])
def add_new_high_score():
    request_data = request.get_json(force=True)

    current_global_highscore = high_score_model.get_the_highest_score()

    # NOTE : playerHighscore will be inserted when is the new player's highscore
    insert_result = high_score_model.insert_new_high_score(request_data["playerHighscore"])
    inserted_player_highscore = high_score_model.get_highscore_by_id(insert_result.inserted_id)

    is_break_the_record = False
    if current_global_highscore["globalHighscore"] == None or request_data["playerHighscore"] < current_global_highscore["globalHighscore"]:
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