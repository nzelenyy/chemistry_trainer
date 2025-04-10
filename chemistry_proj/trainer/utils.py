from .models import ChemFormula
import re

def chem_format(text):
    return re.sub(r'(\d+)', r'<sub>\1</sub>', text)

def write_formula(name, formula):
    new_formula = ChemFormula(name=name, formula=formula)
    new_formula.save()