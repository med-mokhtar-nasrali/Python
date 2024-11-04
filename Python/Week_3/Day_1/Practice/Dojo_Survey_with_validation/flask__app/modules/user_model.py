from flask__app.config.mysqlconnections import connectToMySQL
from flask__app import DB
from flask import flash

class User:
    def __init__(self,data):
        self.name = data["name"]
        self.location = data["location"]
        self.comment = data["comment"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_form(data):
        is_valid = True
        if len(data["name"]) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(data["comment"]) < 10:
            flash("Comment must be at least 10 characters.")
            is_valid = False    
        return is_valid    
    

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojo_survey_schema.dojos (name,location,language,comment) VALUES (%(name)s , %(location)s,%(language)s,%(comment)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def show(cls,data):
        query = "SELECT * FROM dojo_survey_schema.dojos WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        if len(result)< 1 :
            return False
        return cls(result[0])
    
