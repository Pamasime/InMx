from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='index'),
    path('acerca_de_nosotros',views.about,name='about'),
    path('contacto',views.contact,name='contacto')

]
