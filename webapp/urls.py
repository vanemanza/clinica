from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [      
    path('', views.home, name="home"),
    path('servicios/', views.servicios, name="servicios"),  
    path('productos/', views.productos, name="productos"),  
    path('profesionales/', views.profesionales, name="profesionales"),  
    path('contacto/', views.contacto, name="contacto"),       
]

urlpatterns+= static(settings.MEDIA_URL, document_root=str(settings.MEDIA_ROOT))