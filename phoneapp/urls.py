from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name='index'),
    path("", views.lista_smartphones, name='lista_smartphones'),
    path("nuevo/", views.crear_smartphone, name='crear_smartphone'),
]