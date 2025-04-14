"""AppConfig for the trainer Django application.

This module defines the TrainerConfig class which provides configuration
for the trainer app including the default auto field and app name.
"""
from django.apps import AppConfig

class TrainerConfig(AppConfig):
    """Configuration class for the trainer Django application.

    Attributes:
        default_auto_field: Specifies the type of auto-created primary key field.
        name: Specifies the name of the Django application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trainer'
