from flask import Blueprint, jsonify, request
import re
import bcrypt
import os
from app.models import db, User

# Secret pepper (store securely in an environment variable)
PEPPER = os.getenv("PEPPER", "my_secret_pepper")

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET"])
def backend_check():
    """
    just checking to see if the backend is running
    """
    return jsonify({"status": "Backend is running!"}), 200


@auth.route("/create-user", methods=["POST,"])
def create_user():
    try:
        # making sure the necessary valid JSON data is being given
        if not request.json:
            return jsonify({"error": "Invalidor missing JSON data"}), 400
        # manually extracting the data
        data = request.json
        name = data.get("name")
        email = data.get("email")
        hashed_password = data.get("hashed_password")
        # making sure that the information required is submitted
        if not name or not email or not hashed_password:
            return jsonify({"error": "Missing required fields"}), 400

        # validating the email
        email_regex = r"^\S+@\S+\.\S+$"
        if not re.match(email_regex, email):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate password
        password_regex = (
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        )
        if not re.match(password_regex, hashed_password):
            return (
                jsonify(
                    {
                        "error": "Password must include at least one uppercase letter, one lowercase letter, one digit, one special character, and be at least 8 characters long"
                    }
                ),
                400,
            )

        # Pepper and hash the password
        password_with_pepper = hashed_password + PEPPER
        hashed_password = bcrypt.hashpw(password_with_pepper.encode(), bcrypt.gensalt())

        # Check if the user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already registered"}), 400

        # Save the new user
        new_user = User(
            name=name, email=email, hashed_password=hashed_password.decode()
        )
        db.session.add(new_user)
        db.session.commit()

    except Exception as e:
        # error handling
        return jsonify({"error": f"An unexpected error occured: {str(e)}"}), 500
    # success message for validating the data in creating new user
    return jsonify({"message": "User registered successfully!"}), 201
