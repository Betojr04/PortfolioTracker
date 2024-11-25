from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:@localhost/portfolio_tracker"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def welcome():
    print("Welcome to Portfolio Tracker")
    return jsonify({"message": "Portfolio Tracker Backend is running!"})


if __name__ == "__main__":
    app.run(debug=True)
