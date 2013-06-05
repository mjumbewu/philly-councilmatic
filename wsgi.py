import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
CM = os.path.join(ROOT, 'website')

sys.path.insert(0, CM)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
