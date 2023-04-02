from flask import Flask, Blueprint
from flask_cors import CORS
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            static_url_path='/static',
            static_folder="../client/dist/static",
            template_folder="../client/dist"
            )

CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

from server import routes, models
