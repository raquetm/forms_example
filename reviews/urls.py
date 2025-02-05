from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),  # Ruta principal que carga la vista 'review'
    path('thank-you', views.Thank_you_view.as_view()),  # Ruta para la página de agradecimiento
    path('reviews', views.ReviewsListView.as_view()),  # Ruta para la lista de reseñas
    # path('reviews/<int:id>', views.SingleReviewView.as_view()),  # Ruta para una reseña
    path('reviews/<int:pk>', views.SingleReviewView.as_view()),  # Ruta para una reseña


]