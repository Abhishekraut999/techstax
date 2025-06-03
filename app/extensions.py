from flask_pymongo import PyMongo

mongo = PyMongo()

def init_extensions(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/github_events"
    mongo.init_app(app)
