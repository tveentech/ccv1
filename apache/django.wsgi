import os
import sys

sys.path.append('/var/live_code/coffeecastle/ccv1')

os.environ['PYTHON_EGG_CACHE'] = '/var/live_code/coffeecastle/ccv1/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'ccv1.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()