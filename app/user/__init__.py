from flask import Blueprint

# Tạo Blueprint cho module user
user_bp = Blueprint('user', __name__, template_folder='templates')

from . import routes  # Import routes để kích hoạt Blueprint
