"""URL configuration for the trainer application."""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('trainer/', views.trainer, name='trainer'),
    path('trainer/add_formula', views.add_formula, name='add_formula'),
    path("trainer/add_formula_result/", views.add_formula_result, name='add_formula_result'),
    path("trainer/add_substance", views.add_substance, name='add_substance'),
    path("trainer/add_substance_result/", views.add_substance_result, name='add_substance_result'),
    path("trainer/substances_gallery/", views.substances_gallery, name='substances_gallery'),
    path('trainer/substances_gallery/delete_substance', views.delete_substance,
        name='delete_substance'),
    path('trainer/delete_formula', views.delete_formula, name='delete_formula'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
