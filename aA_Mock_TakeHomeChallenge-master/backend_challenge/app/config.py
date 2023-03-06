import os


class Config(object):
    SECRET_KEY = os.eviron.get('SECRET_KEY') or 'this-is-the-secret-key'
