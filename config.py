import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'osdfadnv9qwruj'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '1632141075@qq.com'
    MAIL_PASSWORD = 'wswmnlsxovfyccai'
    ADMINS = ['1632141075@qq.com', ]
    MAIL_DEFAULT_SENDER = '1632141075@qq.com'
    POSTS_PER_PAGE = 3
