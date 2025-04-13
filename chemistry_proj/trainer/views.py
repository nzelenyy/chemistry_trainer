from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import ChemFormula
from .models import SubstanceImg
from . import utils


def trainer(request):
	chemformulas = ChemFormula.objects.all().values()
	template = loader.get_template('formulas_list.html')
	context = {
		'chemformulas': chemformulas,
	}
	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())

def add_formula(request):
	return render(request, 'add_formula.html')

def add_formula_result(request):
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
	else:
		return render(request, "add_substance.html")

def add_substance(request):
	return render(request, 'add_formula.html')

def add_substance_result(request):
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
    else:
        return render(request, "add_substance.html")

def substances_gallery(request):
    images = SubstanceImg.objects.all()
    return render(request, 'substances_gallery.html', {'images': images})

def delete_substance(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        try:
        	utils.remove_substance(image_id)
        except SubstanceImg.DoesNotExist:
            pass
    return redirect('substances_gallery')

def delete_formula(request):
	if request.method == 'POST':
		formula_id = request.POST.get('formula_id')
		if formula_id:
			utils.remove_formula(formula_id)
	return redirect('trainer')





























