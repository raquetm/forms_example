from django.urls import path
from . import views

urlpatterns = [
    path('', views.review),  # Ruta principal que carga la vista 'review'
    path('thank_u', views.thank_u),  # Ruta para la página de agradecimiento
]