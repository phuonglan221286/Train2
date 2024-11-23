from flask import Flask
from .user.models import db
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Sử dụng cấu hình nếu có
    
    db.init_app(app)  # Khởi tạo SQLAlchemy
    with app.app_context():
        db.create_all()  # Tạo bảng nếu chưa tồn tại
    # Import và đăng ký các Blueprint
    from .routes import main_bp
    from .user import user_bp
    from .device import device_bp

    app.register_blueprint(main_bp)  # Đăng ký route chính
    app.register_blueprint(user_bp, url_prefix='/users')  # Đăng ký route user
    app.register_blueprint(device_bp, url_prefix='/devices')  # Đăng ký route user

    return app
