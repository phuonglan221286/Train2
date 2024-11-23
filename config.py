class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Đường dẫn CSDL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///devices.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
