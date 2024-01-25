from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "python_inventory_manager1_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user["first_name"]) <= 0:
            flash("First name is required.", "register")
            is_valid = False
        elif len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters.", "register")
            is_valid = False
        if len(user["last_name"]) <= 0:
            flash("Last name is required.", "register")
            is_valid = False
        elif len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters.", "register")
            is_valid = False
        query = "SELECT * FROM users WHERE EMAIL = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.", "register")
            is_valid = False
        if len(user["email"]) <= 0:
            flash("Email is required.", "register")
            is_valid = False
        elif not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email address.", "register")
            is_valid = False
        if len(user["password"]) <= 0:
            flash("Password is required.", "register")
            is_valid = False
        elif len(user["password"]) < 6:
            flash("Password must be at least 6 characters.", "register")
            is_valid = False
        if user["password"] != user["password_confirmation"]:
            flash("Password and its confirmation must match.", "register")
            is_valid = False
        return is_valid