import os

from dotenv import load_dotenv


load_dotenv() # load environment variables from .env file

BASEDIR = os.path.abspath(os.path.dirname(__name__))
STATIC_FOLDER = os.path.join(BASEDIR, os.environ.get("STATIC_FOLDER"))
TEMPLATE_FOLDER = os.path.join(BASEDIR, os.environ.get("TEMPLATE_FOLDER"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")