from .models import ChemFormula

def write_formula(name, formula):
    new_formula = ChemFormula(name=name, formula=formula)
    new_formula.save()