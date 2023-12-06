from app import app
from flask import Flask, request, jsonify
from app.use_cases.RegisterUser import RegisterUser
from app.adapters.database_adapter import DatabsePort
from app.adapters.User_repository import UserRepository

database_adapter = DatabsePort()
# @app.route("/register", methods=["POST"])
class RegisterUsers:
    pass
def register_user():
    user = request.get_json()
    user_repo = UserRepository(database_adapter)
    register_user = RegisterUser(user_repo)
    register_user.execute(user)
    return jsonify({"message": "User created successfully"}), 201


