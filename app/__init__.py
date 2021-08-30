import os

from flask import Flask, request, send_from_directory

from flask_cors import CORS

from .main import main_bp
from .api import api_bp

from config import Config, BASEDIR, STATIC_FOLDER, TEMPLATE_FOLDER


def create_app():
    # set static_folder and template_folder attributenof flask app to point to
    # vue build directory where assets and templates files are saved.
    app = Flask(
        __name__,
        static_folder=STATIC_FOLDER,
        template_folder=TEMPLATE_FOLDER
    )
    app.config.from_object(Config)

    # custom routes to serve static files for vue frontend app
    @app.route('/js/<path:filename>')
    @app.route('/css/<path:filename>')
    @app.route('/img/<path:filename>')
    def serve_static(filename):
        # split request.path to get static sub-directory to properly build static path
        sub_dir = [value for value in request.path.split('/') if value != ""][0]
        static_path = os.path.join(BASEDIR, 'frontend', 'dist', sub_dir)
        return send_from_directory(static_path, filename)
    
    # Register extensions
    CORS(app)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    return app
