from settings import *
import os

with os.open('/etc/sitdinner/db-password', 'rb') as f:
    db_password = f.readline()

DEBUG = True

DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'sitdinner'
DATABASE_USER = 'sitdinner'             # Not used with sqlite3.
DATABASE_PASSWORD = db_password

DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

sys.stdout = sys.stderr
