import os

from flask import Flask
from .config import Configuration
from .models import db
from app import routes

app = Flask(__name__)
app.config.from_object(Configuration)
DB_FILE = os.environ.get("DATABASE_URL")
db.init_app(app)

app.register_blueprint(routes.bp)


with app.app_context():
	db.drop_all()
	db.create_all()
