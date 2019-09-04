import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'osdfadnv9qwruj'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'mail.longmaster.com.cn'
    MAIL_PORT = 110
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = 'linhai@longmaster.com.cn'
    MAIL_PASSWORD = 'www.4399.com'
    ADMINS = ['linhai@longmaster.com.cn']
