from flask import Blueprint

device_bp = Blueprint('device', __name__, template_folder='templates')

from . import routes
