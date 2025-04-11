from django.shortcuts import render
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
	name = request.POST.get("name")
	formula = request.POST.get("formula")
	utils.write_formula(name, formula)
	return render(request, "add_formula_result.html")

def add_substance(request):
	return render(request, 'add_substance.html')

def add_substance_result(request):
	name = request.POST.get("name")
	image = request.FILES.get("substance")
	utils.write_substance(name, image)
	return render(request, "add_substance_result.html")

def substances_gallery(request):
    images = SubstanceImg.objects.all()
    return render(request, 'substances_gallery.html', {'images': images})
