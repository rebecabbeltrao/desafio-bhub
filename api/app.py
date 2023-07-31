import os
from dotenv import load_dotenv
from flask import Flask
from api.database.models import db
from api.service.routes import app_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__, instance_relative_config=True)

app.config['MONGODB_SETTINGS'] = [
    {
        "db": os.environ.get('DATABASE_NAME'),
        "host": os.environ.get("DATABASE_HOST"),
        "port": int(os.environ.get("DATABASE_PORT"))
    }
]

db.init_app(app)
app.register_blueprint(app_bp)

app.run(port=5000, host='localhost', debug=True)
