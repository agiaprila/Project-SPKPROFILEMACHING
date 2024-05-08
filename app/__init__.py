# __init__.py

from flask import Flask
from flask_mysqldb import MySQL
from config import Config

# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi koneksi MySQL
mysql = MySQL(app)

# Import modul routes untuk rute aplikasi
from app import routes