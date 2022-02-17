from flask import Blueprint
from flask import Flask,bootstrap
main = Blueprint('main',__name__)
from . import views,errors
from main import main as main_blueprint
