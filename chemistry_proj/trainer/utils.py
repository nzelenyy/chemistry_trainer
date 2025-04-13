import os
import re

from .models import ChemFormula
from .models import SubstanceImg
from django.conf import settings


def sub_format(text):
    return re.sub(r'(\d+)', r'<sub>\1</sub>', text)

def write_formula(name, formula):
    new_formula = ChemFormula(name=name, formula=sub_format(formula))
    new_formula.save()

def write_substance(name, substance):
    new_substance = SubstanceImg(name=name, image=substance)
    new_substance.save()

def remove_substance(image_id):
    substance = SubstanceImg.objects.get(id=int(image_id))

    if substance.image:
        file_path = os.path.join(settings.MEDIA_ROOT, str(substance.image))
        if os.path.exists(file_path):
            os.remove(file_path)

    substance.delete()

def remove_formula(formula_id):
    formula = ChemFormula.objects.get(id=int(formula_id))
    formula.delete()