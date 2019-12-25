from flask.cli import FlaskGroup
from project import app, db
from project.model.high_score import HighScore

cli = FlaskGroup(app)


@cli.command("clear_data")
def clear_collection():
    db.drop_collection(HighScore.__collection__)


if __name__ == "__main__":
    cli()
