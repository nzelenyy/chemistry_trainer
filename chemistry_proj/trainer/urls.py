from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('trainer/', views.trainer, name='trainer'),
    path('trainer/add_formula', views.add_formula, name='add_formula'),
    path("trainer/add_formula_result/", views.add_formula_result, name='add_formula_result'),
]