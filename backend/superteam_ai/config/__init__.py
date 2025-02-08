






from . import routesapp.config.from_object(Config)app = Flask(__name__)from .config import Configfrom flask import Flask