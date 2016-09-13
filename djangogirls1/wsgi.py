"""
WSGI config for djangogirls1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangogirls1.settings")

application = get_wsgi_application()

#import os
#import sys

#path ='/home/johnson/downloads/python_workspace/djangogirls1'
#if path not in sys.path:
#    sys.path.append(path)

#os.environ['DJANGO_SETTINGS_MODULE'] = 'djangogirls1.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()



