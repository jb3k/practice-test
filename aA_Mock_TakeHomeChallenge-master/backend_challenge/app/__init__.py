from flask import Flask
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

# @app.route('/')

app.register_blueprint()

db.init_app(app)
Migrate(app, db)    



def index():
    return '<h1>Hello World</h1>'
