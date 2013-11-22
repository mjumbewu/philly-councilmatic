import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
CM = os.path.join(ROOT, 'website')

sys.path.insert(0, CM)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application)