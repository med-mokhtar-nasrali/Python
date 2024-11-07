from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash



class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.recipe_name = data["recipe_name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date = data["date"]
        self.under_time = data["under_time"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.posted_by = ""
    

    @classmethod
    def create(cls,data):
        query = """
                INSERT INTO recipes (recipe_name,description,instructions,date,under_time,user_id)
                VALUES (%(recipe_name)s,%(description)s,%(instructions)s,%(date)s,%(under_time)s,%(user_id)s)
                """
        return connectToMySQL( DB ).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id;
                """
        results = connectToMySQL( DB ).query_db(query)
        all_recipes = []
        for row in results:
            recipe = cls(row)
            recipe.posted_by= f'{row["first_name"]}{row["last_name"]}'
            all_recipes.append(recipe)
        return all_recipes
    

    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s
                """
        result = connectToMySQL( DB ).query_db(query,data)
        recipe = cls(result[0])
        recipe.posted_by = f'{result[0]["first_name"]}{result[0]["last_name"]}'
        return recipe
    
    @classmethod
    def update(cls,data):
        query = """
                UPDATE recipes SET
                recipe_name = %(recipe_name)s,
                description = %(description)s,
                instructions = %(instructions)s,
                date = %(date)s,
                under_time = %(under_time)s
                WHERE recipes.id = %(id)s;
                """
        return connectToMySQL( DB ).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = """
                DELETE FROM recipes WHERE id = %(id)s;
                """
        return connectToMySQL( DB ).query_db(query,data)




    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["recipe_name"])<3:
            is_valid = False
            flash("Name is too short","recipe_name")
        if len(data["description"])<3:
            is_valid = False
            flash("description is too short","description")
        if len(data["instructions"])<3:
            is_valid = False
            flash("instructions is too short","instructions")
        if data['date']=="":
            is_valid = False
            flash('Date is REQUIRED',"date")   
        return is_valid
        