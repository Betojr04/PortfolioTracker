from flask import Blueprint, jsonify

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET"])
def backend_check():
    """
    just checking to see if the backend is running
    """
    return jsonify({"status": "Backend is running!"}), 200
