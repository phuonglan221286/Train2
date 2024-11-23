from flask import Blueprint, render_template

# Khởi tạo Blueprint
main_bp = Blueprint('main', __name__)

# Định nghĩa route cho trang chủ
@main_bp.route('/')
def home():
    return render_template('index.html')

# Định nghĩa route cho trang About
@main_bp.route('/about')
def about():
    return render_template('about.html')
