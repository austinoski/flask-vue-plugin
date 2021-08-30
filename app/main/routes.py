
from flask import render_template

from . import main_bp as app


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
