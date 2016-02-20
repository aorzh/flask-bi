#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:5000/bi'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_CONNECT_OPTIONS = {}
    STATIC = os.path.join(os.path.dirname(__file__), 'static')
    MAIN_DATABASE = "mysql://root:root@localhost:5000/arik.dev"
    NEW_DATABASE = "mysql://root:root@localhost:5000/bi3"
