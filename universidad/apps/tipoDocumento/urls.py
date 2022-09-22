from django.urls import path, re_path, include
from . import views

urlpatterns = [
   path('', views.inicio,name='inicio'),
   path('documento', views.documento,name='documento'),
   path('documento/crear', views.crear,name='crear'),
   path('documento/borrar/<int:id>', views.borrar,name='borrar'),
   path('documento/editar/<int:id>', views.editar,name='editar'),
]
