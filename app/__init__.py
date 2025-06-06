from flask import Flask
from app.views import webhook_bp
from app.extensions import mongo

def create_app():
    app = Flask(__name__)
    
    app.config["MONGO_URI"] = "mongodb://localhost:27017/webhook_db"  # update as needed

    mongo.init_app(app)

    app.register_blueprint(webhook_bp)

    return app
