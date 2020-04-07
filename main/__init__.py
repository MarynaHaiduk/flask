from flask import Flask
from flask_bootstrap import Bootstrap
import os

def create_app(test_config=None):
    app = Flask(__name__)
    Bootstrap(app)

    my_sekret_key = os.urandom(24)
    app.config['SECRET_KEY'] = 'X\x18#L\xeb\xda\xe6nc\x19\xfdU_?\x02\xd4\xbf\xda\xd9\x8b0\x1e?\x8d'

    return app