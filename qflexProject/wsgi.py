# wsgi.py

"""
WSGI config for qflexProject project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qflexProject.settings')

application = get_wsgi_application()
