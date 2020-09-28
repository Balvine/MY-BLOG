from flask import flask
from flask_sqalchemy import SQALCHEMY


db = SQALCHEMY()
def create_app():
    app = Flak(_name_)
    app.config()
    