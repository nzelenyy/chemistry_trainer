from .models import ChemFormula
from .models import SubstanceImg
import re

def sub_format(text):
    return re.sub(r'(\d+)', r'<sub>\1</sub>', text)

def write_formula(name, formula):
    new_formula = ChemFormula(name=name, formula=sub_format(formula))
    new_formula.save()

def write_substance(name, substance):
    new_substance = SubstanceImg(name=name, image=substance)
    new_substance.save()