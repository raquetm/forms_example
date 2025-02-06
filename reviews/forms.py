from django import forms  # Importamos el módulo forms de Django para crear formularios
from .models import Review, Student  # Importamos el modelo Review y el modelo Student

### A) PRIMERA FORMA DE DEFINIR EL FORMULARIO UTILIZANDO forms.Form
# class ReviewForm(forms.Form):
#     # Campo para el nombre del usuario
#     user_name = forms.CharField(
#         label="Name:",  # Etiqueta que se mostrará en el formulario
#         required=False,  # El campo no es obligatorio
#         max_length=100,  # Longitud máxima de 100 caracteres
#         error_messages={  # Mensajes de error personalizados
#             "required": "Your name mustn't be empty (╥﹏╥)",  # Si el campo está vacío
#             "max_length": "Please enter a shorter name (╥﹏╥)"  # Si excede la longitud máxima
#         }
#     )
#     # Campo para la reseña del usuario (feedback)
#     review_text = forms.CharField(
#         label="Your feedback",  # Etiqueta para el campo
#         required=False,  # No es obligatorio
#         widget=forms.Textarea,  # Se muestra como un área de texto en lugar de un input de una sola línea
#         max_length=200  # Máximo de 200 caracteres
#     )
#     # Campo para la calificación (rating)
#     rating = forms.IntegerField(
#         label="Your rating",  # Etiqueta para el campo
#         required=False,  # No es obligatorio
#         min_value=1,  # Valor mínimo permitido
#         max_value=5  # Valor máximo permitido
#     )

### B) FORMA MÁS CORTA UTILIZANDO forms.ModelForm
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # Especificamos el modelo que usaremos
        fields = '__all__'  # Usamos todos los campos del modelo
        labels = {
            "user_name": "Your Name",  # Etiqueta para el campo 'user_name'
            "review_text": "Your Review",  # Etiqueta para el campo 'review_text'
            "rating": "Your Rating"  # Etiqueta para el campo 'rating'
        }
        error_messages = {
            "user_name": {
                "required": "Your name is required (╥﹏╥)",  # Mensaje si el campo 'user_name' está vacío
                "max_length": "Your name must be shorter than 100 characters (╥﹏╥)"  # Mensaje si el nombre es muy largo
            },
            "review_text": {
                "max_length": "Your review must be shorter than 200 characters (╥﹏╥)"  # Mensaje si la reseña es muy larga
            }
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','degree']
