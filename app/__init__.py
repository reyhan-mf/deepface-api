from flask import Flask

app = Flask(__name__, template_folder='D:/venv-test/templates')

from app import routes
