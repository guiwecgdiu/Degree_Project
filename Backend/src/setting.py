import os

basedir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_EMAIL = ['ysytql@163.com','admin@163.com','han@163.com','aren@163.com','zhang@163.com','all@163.com']

    OVERALL_UPLOAD_PATH=os.path.join(basedir,'uploads')

    PHOTO_SIZE={'small':400,'medium':400}
    PHOTO_SUFFIX = {
        PHOTO_SIZE['small']:'_s',
        PHOTO_SIZE['medium']:'_m'
    }

    PET_UPLOAD_PATH = os.path.join(OVERALL_UPLOAD_PATH, 'pets')
    PET_DEFAULT_PATH = os.path.join(OVERALL_UPLOAD_PATH, 'default')

    AVATARS_SAVE_PATH =os.path.join(OVERALL_UPLOAD_PATH,'avatars')
    AVATAR_SIZE_TUPLE=(30,100,200)

    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = 'wsdsgbxd@163.com'
    MAIL_PASSWORD = 'VLEMBIFMETRSMLCJ'
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = ('YSY', 'MAIL_USERNAME')

    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 1
    MAX_CONTENT_LENGTH = 3 * 1024 * 1024
    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_ENABLE_CRSF = True

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'hospital.db')

class TestingConfig(BaseConfig):
    TESTING =True
    WTF_CSRF_ENABLED=False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'hospital.db')

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.db')


config= {
        'development':DevelopmentConfig,
        'testing':TestingConfig,
        'production':ProductionConfig
    }
