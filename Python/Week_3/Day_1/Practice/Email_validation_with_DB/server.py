from flask_app import app
from flask_app.controllers import user_controller 
app.secret_key="12355"
if __name__ == "__main__":
    app.run(debug=True)