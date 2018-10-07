from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


##########################
# Aufgrund dem Namen '__init__' ist diese Datei die sogenannte 'Erste Datei',
# die bei einem 'import flaskapp from ...' kontrolliert wird
##########################


# Ausführen der Applikation
app = Flask(__name__)
app.config['SECRET_KEY'] = '2b4311fdf854371c367d26a90e81b2d0'
# Datenbank erstellen
# Das **from flask_sqlalchemy import SQLAlchemy** gehört ebenfalls dazu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Passwörter werden geschlüsselt
bcrypt = Bcrypt(app)

from flaskapp import routes