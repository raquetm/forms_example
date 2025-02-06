from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField(max_length=200)
    rating = models.IntegerField()

class Student(models.Model): #esto es el modelo Student para empezar el ejercicio 5.4
    name=models.CharField(max_length=200)
    degree=models.CharField(max_length=100)