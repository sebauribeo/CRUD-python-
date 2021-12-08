from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('editar/<int:id>', views.editar, name = 'editar'),
    path('eliminar/<int:id>', views.eliminar, name = 'eliminar'),
]