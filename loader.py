from flask import Flask
from flask_bootstrap import Bootstrap

from api import ProjectsManager

app = Flask(__name__)
app.secret_key = '123:abc'
Bootstrap(app)
pm = ProjectsManager('http://my-bots.ru:5001')
