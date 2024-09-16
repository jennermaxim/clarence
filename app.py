from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hospital.routes import hospital_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.register_blueprint(hospital_bp, url_prefix='/hospital')

if __name__ == "__main__":
    app.run(ssl_context='adhoc', debug=True)
