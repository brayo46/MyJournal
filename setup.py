from distutils.core import setup

setup(
    name='Journal',
    version='1.0',
    packages=['flask',
              'alembic',
              'gunicorn',
              'psycopg2',
              'flask_jwt',
              'flask_cors',
              'flask_restplus',
              'flask_sqlalchemy',
              'sqlalchemy_paginator',
              'flask_restful_swagger'],
    url='',
    license='',
    author='Muhumuza Brian',
    author_email='muhumuzabri@gmail.com',
    description='A very simple app '
)
