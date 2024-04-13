from django.apps import AppConfig
from django.db.models import BigAutoField

class NetworkConfig(AppConfig):
    name = 'network'
    default_auto_field = 'django.db.models.BigAutoField'
