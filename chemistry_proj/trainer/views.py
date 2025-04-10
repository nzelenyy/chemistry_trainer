from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ChemFormula

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