from flask import Flask
from app.models import db

from app.routes.auth_routes import auth


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+mysqlconnector://root:@localhost/portfolio_tracker"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    app.register_blueprint(auth)

    return app
