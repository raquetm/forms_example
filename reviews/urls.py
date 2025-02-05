from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),  
    # Ruta principal ('/') que carga la vista ReviewView.
    # Esta vista maneja la creación de reseñas utilizando CreateView.

    path('thank-you', views.Thank_you_view.as_view()),  
    # Ruta '/thank-you' que carga la vista de agradecimiento Thank_you_view.

    path('reviews', views.ReviewsListView.as_view()),  
    # Ruta '/reviews' que carga la vista ReviewsListView.
    # Muestra la lista de todas las reseñas almacenadas en la base de datos.

    # path('reviews/<int:id>', views.SingleReviewView.as_view()),  
    # Versión antigua de la ruta para mostrar una sola reseña.
    # Usaba TemplateView y requería extraer el ID manualmente en views.py.

    path('reviews/<int:pk>', views.SingleReviewView.as_view()),  
    # Nueva versión de la ruta para mostrar una sola reseña utilizando DetailView.
    # 'pk' (Primary Key) es el nombre que DetailView espera por defecto para identificar registros.
]