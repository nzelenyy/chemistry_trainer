"""Models module defines database models for the trainer application."""

from django.db import models


class ChemFormula(models.Model):
    """Model for storing chemical formulas and their names."""
    name = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)


class SubstanceImg(models.Model):
    """Model for storing substance images with their names."""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
