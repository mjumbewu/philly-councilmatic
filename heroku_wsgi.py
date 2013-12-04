import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
CM = os.path.join(ROOT, 'src')

sys.path.insert(0, CM)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
from dj_static import Cling
application = Cling(django.core.handlers.wsgi.WSGIHandler())
