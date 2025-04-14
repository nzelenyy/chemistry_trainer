"""Django admin configuration for the trainer application.

This module registers the application's models with the Django admin interface,
allowing for CRUD operations through the admin panel.
"""

from django.contrib import admin
from .models import ChemFormula, SubstanceImg

admin.site.register(ChemFormula)
admin.site.register(SubstanceImg)
