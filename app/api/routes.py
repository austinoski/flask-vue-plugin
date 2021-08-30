from flask import jsonify, url_for

from . import api_bp as app


database = {}

@app.route('/install', methods=["GET"])
def install_api():
    data = {
        "name": "Sample Plugin",
        "description": "Simple proof of concept plugin in flask",
        "sidebar_url": url_for('api.sidebar_api', _external=True),
        "install_url": url_for('api.install_api', _external=True),
        "template_url": url_for('main.index', _external=True)
    }
    return jsonify(data), 200


@app.route('/sidebar', methods=["GET"])
def sidebar_api():
    data = {
        "icon": "Hello World",
        "text": "Channel name"
    }
    return jsonify(data), 200
