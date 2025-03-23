"""
WSGI config for definitions_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.conf import settings
settings.configure(
    ALLOWED_HOSTS=['*'], 
    STATIC_ROOT=os.path.join(os.getcwd(), 'staticfiles'),
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'definitions_project.settings')

application = get_wsgi_application()
app = application
