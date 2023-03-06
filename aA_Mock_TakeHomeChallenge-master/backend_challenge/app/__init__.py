from flask import Flask
from flask_migrate import Migrate

from app.models import db
from app.config import Config
from app.api.coffee_routes import coffee_routes
from app.api.post_routes import post_routes


app = Flask(__name__)
app.config.from_object(Config)

# @app.route('/')

app.register_blueprint(coffee_routes, url_prefix='/api/coffee')
app.register_blueprint(post_routes, url_prefix='/api/post')
db.init_app(app)
Migrate(app, db)    



def index():
    return '<h1>Hello World</h1>'
