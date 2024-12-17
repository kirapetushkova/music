import os

class Config:
    SECRET_KEY = 'your_secret_key'
    
    base_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(base_dir, "instance", "site.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    print(f"Database URI: {SQLALCHEMY_DATABASE_URI}")