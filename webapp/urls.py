from django.urls import path
from . import views 

urlpatterns = [      
    path('', views.home, name="home"),
    path('servicios/', views.servicios, name="servicios"),  
    path('productos/', views.productos, name="productos"),  
    path('profesionales/', views.profesionales, name="profesionales"),  
    path('contacto/', views.contacto, name="contacto"),       
]