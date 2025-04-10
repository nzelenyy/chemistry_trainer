from django.db import models

class ChemFormula(models.Model):
	name = models.CharField(max_length=255)
	formula = models.CharField(max_length=255)

