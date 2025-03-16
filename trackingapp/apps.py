#################################################################
# file: trackingapp/apps.py
#################################################################
from django.apps import AppConfig

class TrackingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trackingapp'

    def ready(self):
        import trackingapp.signals  # For signal processing such as logging
