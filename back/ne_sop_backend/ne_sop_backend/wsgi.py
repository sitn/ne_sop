"""
WSGI config for ne_sop_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

# replace path here with the root path of your app
root="D:/applications/NESOP/prepub/back"

sys.path = [
    root + "/ne_sop_backend",
    root + "/venv/Scripts",
    root + "/venv/Lib",
    root + "/venv/Lib/site-packages",
    ] + sys.path


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ne_sop_backend.settings')

application = get_wsgi_application()
