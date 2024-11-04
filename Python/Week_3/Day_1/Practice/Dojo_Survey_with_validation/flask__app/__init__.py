from flask import Flask,session
app = Flask(__name__)
DB = "dojo_survey_schema"
app.secret_key="123456"