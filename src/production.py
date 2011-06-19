from settings import *
import sys

f = open('/etc/sitdinner/db-password', 'rb')
db_password = f.readline()

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sitdinner',
        'USER': 'sitdinner',            # Not used with sqlite3.
        'PASSWORD': db_password,

        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',            # Set to empty string for default. Not used with sqlite3.
    }
}
sys.stdout = sys.stderr
