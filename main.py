from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:@localhost/portfolio_tracker"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    hashed_password = db.Column(
        db.String(1000),
        nullable=False,
    )

    portfolios = db.relationship(
        "Portfolio", back_populates="user", cascade="all, delete-orphan"
    )


class Portfolio(db.Model):
    __tablename__ = "portfolios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relatinship("User", back_populates="portfolios")


@app.route("/")
def welcome():
    print("Welcome to Portfolio Tracker")
    return jsonify({"message": "Portfolio Tracker Backend is running!"})


if __name__ == "__main__":
    app.run(debug=True)
