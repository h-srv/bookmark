from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
api = Api(version='1.0', title='Bookmark', description='A simple bookmark API service')
ma = Marshmallow()
