from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "admin.login"

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "supersecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tneadb.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    
    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    from app.admin_routes import admin
    app.register_blueprint(admin)

    return app
from app.models import Admin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))