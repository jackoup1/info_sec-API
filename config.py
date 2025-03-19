import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'abbasa was here')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/info_sec'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
