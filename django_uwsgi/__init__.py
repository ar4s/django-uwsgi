__version__ = '0.2.0'


try:
    import uwsgi
except ImportError:
    uwsgi = None

try:
    import cPickle as pickle
except ImportError:
    import pickle

default_app_config = 'django_uwsgi.apps.DjangoUwsgiConfig'
