"""View functions for the trainer application.

This module handles all web requests for the chemistry trainer app,
including formula management, substance image handling, and gallery views.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import ChemFormula, SubstanceImg
from . import utils


def trainer(request):
    """Render the main trainer page with list of chemical formulas."""
    chemformulas = ChemFormula.objects.all().values()  # pylint: disable=no-member
    template = loader.get_template('formulas_list.html')
    context = {
        'chemformulas': chemformulas,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    """Render the main page of the application."""
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def add_formula(request):
    """Display the form for adding new chemical formulas."""
    return render(request, 'add_formula.html')


def add_formula_result(request):
    """Process the submitted chemical formula and display results."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        formula = request.POST.get("formula", "").strip()
        if not name:
            context = {
                "success": False,
                "comment": "Название формулы не может быть пустым"
            }
        elif not formula:
            context = {
                "success": False,
                "comment": "Формула не должна быть пустой"
            }
        else:
            utils.write_formula(name, formula)
            context = {
                "success": True,
                "comment": "Формула успешно добавлена"
            }
        return render(request, "add_formula_result.html", context)
    return render(request, "add_substance.html")


def add_substance(request):
    """Display the form for adding new substance images."""
    return render(request, 'add_substance.html')


def add_substance_result(request):
    """Process the submitted substance image and display results."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        image = request.FILES.get("substance")
        if not name:
            context = {
                "success": False,
                "comment": "Название вещества не может быть пустым"
            }
        elif not image:
            context = {
                "success": False,
                "comment": "Не выбрано изображение вещества"
            }
        else:
            allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
            if not any(image.name.lower().endswith(ext) for ext in allowed_extensions):
                context = {
                    "success": False,
                    "comment": "Недопустимый формат изображения. Допустимы: JPG, PNG, GIF, BMP"
                }
            elif image.size > 15 * 1024 * 1024:
                context = {
                    "success": False,
                    "comment": "Размер изображения не должен превышать 15 MB"
                }
            else:
                utils.write_substance(name, image)
                context = {
                    "success": True,
                    "comment": "Вещество успешно добавлено"
                }

        return render(request, "add_substance_result.html", context)
    return render(request, "add_substance.html")


def substances_gallery(request):
    """Display gallery of all uploaded substance images."""
    images = SubstanceImg.objects.all()  # pylint: disable=no-member
    return render(request, 'substances_gallery.html', {'images': images})


def delete_substance(request):
    """Handle deletion of substance images."""
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        try:
            utils.remove_substance(image_id)
        except SubstanceImg.DoesNotExist:  # pylint: disable=no-member
            pass
    return redirect('substances_gallery')


def delete_formula(request):
    """Handle deletion of chemical formulas."""
    if request.method == 'POST':
        formula_id = request.POST.get('formula_id')
        if formula_id:
            utils.remove_formula(formula_id)
    return redirect('trainer')
