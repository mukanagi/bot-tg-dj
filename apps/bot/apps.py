from django.apps import AppConfig
from django.db import models

class BotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "mybothobot.apps.bot"
