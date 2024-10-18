from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from data.create_table import create_table


app = Flask(__name__)
# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.path.dirname(__file__), "data/data_performance.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB_PATH = 'data/data_performance.db'

db = SQLAlchemy(app)  # Initialiser SQLAlchemy avec l'application

app.secret_key = 'cekds54654gfdq353fsdqjfie0255612'

from routes import *  # Importer les routes ici

if not os.path.exists(DB_PATH):
    create_table(DB_PATH)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


