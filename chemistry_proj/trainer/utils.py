"""Utility functions for chemical formula processing and database operations."""

import os
import re
from django.conf import settings
from .models import ChemFormula, SubstanceImg


def sub_format(text: str) -> str:
    """Convert numbers in text to HTML subscript format.
    
    Args:
        text: Input string containing numbers to be converted
        
    Returns:
        String with numbers wrapped in <sub> tags
    """
    return re.sub(r'(\d+)', r'<sub>\1</sub>', text)


def write_formula(name: str, formula: str) -> None:
    """Save a new chemical formula to the database.
    
    Args:
        name: Name of the chemical formula
        formula: The chemical formula string
    """
    new_formula = ChemFormula(name=name, formula=sub_format(formula))
    new_formula.save()


def write_substance(name: str, substance) -> None:
    """Save a new substance image to the database.
    
    Args:
        name: Name of the substance
        substance: Image file of the substance
    """
    new_substance = SubstanceImg(name=name, image=substance)
    new_substance.save()


def remove_substance(image_id: int) -> None:
    """Remove a substance image from database and delete the associated file.
    
    Args:
        image_id: ID of the substance image to remove
    """
    substance = SubstanceImg.objects.get(id=int(image_id)) # pylint: disable=no-member

    if substance.image:
        file_path = os.path.join(settings.MEDIA_ROOT, str(substance.image))
        if os.path.exists(file_path):
            os.remove(file_path)

    substance.delete()


def remove_formula(formula_id: int) -> None:
    """Remove a chemical formula from the database.
    
    Args:
        formula_id: ID of the formula to remove
    """
    formula = ChemFormula.objects.get(id=int(formula_id)) # pylint: disable=no-member
    formula.delete()
