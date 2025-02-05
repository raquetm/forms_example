from django import forms  # Importamos el módulo forms de Django para crear formularios

# Definimos un formulario llamado ReviewForm
class ReviewForm(forms.Form):
    # Campo para el nombre del usuario
    user_name = forms.CharField(
        label="Name:",  # Etiqueta que se mostrará en el formulario
        required=False,  # El campo no es obligatorio
        max_length=100,  # Longitud máxima de 100 caracteres
        error_messages={  # Mensajes de error personalizados
            "required": "Your name mustn't be empty (╥﹏╥)",  # Si el campo está vacío
            "max_length": "Please enter a shorter name (╥﹏╥)"  # Si excede la longitud máxima
        }
    )

    # Campo para la reseña del usuario (feedback)
    review_text = forms.CharField(
        label="Your feedback",  # Etiqueta para el campo
        required=False,  # No es obligatorio
        widget=forms.Textarea,  # Se muestra como un área de texto en lugar de un input de una sola línea
        max_length=200  # Máximo de 200 caracteres
    )

    # Campo para la calificación (rating)
    rating = forms.IntegerField(
        label="Your rating",  # Etiqueta para el campo
        required=False,  # No es obligatorio
        min_value=1,  # Valor mínimo permitido
        max_value=5  # Valor máximo permitido
    )
