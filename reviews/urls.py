from django.urls import path
from . import views

urlpatterns = [
    path('', views.review),
    path('thank_u', views.thank_u),
]