from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flasgger import Swagger
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
swagger = Swagger()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    swagger.init_app(app)
    CORS(app)
    api = Api(app)

    # Register routes
    from app.routes import register_routes
    register_routes(api)

    return app
