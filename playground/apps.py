from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig



class playgroundAdminConfig(AdminConfig):
    default_site = 'playground.admin.PlaygroundAdminSite'
    
class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'