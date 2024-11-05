from flask_app.config.mysqlconnections import connectToMySQL
from flask_app import DB
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data["id"]
        self.email=data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def insert_email(cls,data):
        query = "INSERT INTO users (email) VALUES (%(email)s);"
        result = connectToMySQL(DB).query_db(query,data)
        return result
    
    @staticmethod
    def email_validation(data):
        is_valid=True
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address!","email_validation")
            is_valid = False
        return is_valid    

    @classmethod
    def get_by_id(cls, data):
        query = " select * from users where id = %(id)s ;" 
        result = connectToMySQL(DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query) 
        users = []
        for row in results:
            users.append(cls(row))
        return users
