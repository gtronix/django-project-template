from django.apps import AppConfig
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class ThemeConfig(AppConfig):
    name = 'theme'
