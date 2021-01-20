###################
# backend/apps.py
#
# This is a basic app configuration
# to allow django to detect that the
# backend actually exists here.
###################
from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'backend'
    verbose_name = "Dartboard Backend"
