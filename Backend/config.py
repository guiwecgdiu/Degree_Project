import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'hospital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CV_UPLOAD_DIR = os.path.join(basedir, 'uploaded_CV')
    PH_UPLOAD_DIR = os.path.join(basedir,'src', 'static', 'uploaded_PH')
    FLASK_APP= 'start.py'

    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'wsdsgbxd@163.com'
    MAIL_PASSWORD = 'VLEMBIFMETRSMLCJ'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = ('YSY', 'MAIL_USERNAME')


class ProductConfig(Config):
    pass