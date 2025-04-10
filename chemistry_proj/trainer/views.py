from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ChemFormula
from . import utils


def trainer(request):
	chemformulas = ChemFormula.objects.all().values()
	template = loader.get_template('formulas_list.html')
	context = {
		'chemformulas': chemformulas,
	}
	return HttpResponse(template.render(context, request))

# def trainer(request):
# 	names = ChemFormula.objects.values_list('name', flat=True)
# 	formulas = ChemFormula.objects.values_list('formula', flat=True)
# 	template = loader.get_template('formulas_list.html')
# 	context = {
# 		'names': names,
# 		'formulas': utils.chem_format(formulas),
# 	}
# 	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())

def add_formula(request):
	return render(request, 'add_formula.html')

def add_formula_result(request):
	name = request.POST.get("name")
	formula = request.POST.get("formula")
	utils.write_formula(name, utils.chem_format(formula))
	return render(request, "add_formula_result.html")