#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'dsofpkoasodksap'
    SECRET_KEY = 'zxczxasdsad'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:5000/bi'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ADMINS = frozenset(['al.orzh@gmail.com'])
    DATABASE_CONNECT_OPTIONS = {}
    THREADS_PER_PAGE = 8
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    RECAPTCHA_OPTIONS = {'theme': 'white'}
    STATIC = os.path.join(os.path.dirname(__file__), 'static')

    # Flask-Mail settings
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'yourmail')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'pass')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '"BI dashboard" <noreply@example.com>')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
    MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL', True))

    # Flask-User settings
    USER_APP_NAME = "BI dashboard"  # Used by email templates


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

