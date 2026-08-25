# import os
# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# # load_dotenv(os.path.join(basedir, '.env'))

# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'tasks.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     ROOT_PATH = basedir
#     STATIC_FOLDER = os.path.join(basedir, 'app//static')
#     TEMPLATE_FOLDER_MAIN = os.path.join(basedir, 'app//main//templates')
#     TEMPLATE_FOLDER_ERRORS = os.path.join(basedir, 'app//errors//templates')

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app//static')
    TEMPLATE_FOLDER_MAIN = os.path.join(basedir, 'app//main//templates')
    TEMPLATE_FOLDER_PROJECTS = os.path.join(basedir, 'app//projects//templates')