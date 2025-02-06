from django.shortcuts import render  # Función para renderizar plantillas
from django.http import HttpResponseRedirect  # Para redirigir después de enviar un formulario
from .forms import ReviewForm, StudentForm  # Importamos el formulario de reseñas y el de estudiantes
from .models import Review, Student  # Importamos el modelo de reseñas y el modelo de estudiantes
from django.views import View  # Clase base para vistas basadas en clases 
from django.views.generic.base import TemplateView  # Vista genérica para renderizar plantillas
from django.views.generic import ListView, DetailView, UpdateView  # Vistas genéricas para listar y detallar objetos
from django.views.generic.edit import FormView, CreateView, DeleteView  # Vistas genéricas para manejar formularios
from django.urls import reverse_lazy

### A) VISTA PARA GESTIONAR LAS RESEÑAS UTILIZANDO CLASES
## 1.1. PRIMERA FORMA DE DEFINIR LA CLASE ReviewView UTILIZANDO View
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()  # Se crea un formulario vacío para la reseña
#         return render(request, "reviews/review.html", {"form": form})  # Se pasa el formulario a la plantilla
#     def post(self, request):
#         form = ReviewForm(request.POST)  # Se llena el formulario con los datos del usuario
#         if form.is_valid():  # Se valida el formulario
#             form.save()  # Se guarda la reseña en la base de datos
#             return HttpResponseRedirect("/thank-you")  # Redirige a la página de agradecimiento
#         return render(request, "reviews/review.html", {"form": form})  # Si hay errores, se vuelve a mostrar el formulario con mensajes de error
# # Vista para la página de agradecimiento
# def thank_you(request):
#     return render(request, "reviews/thank_you.html")  # Renderiza la página de agradecimiento

## 1.2. FORMA MÁS CORTA UTILIZANDO FormView
# class ReviewView(FormView):
#     form_class = ReviewForm  # Se usa el formulario ReviewForm
#     template_name = "reviews/review.html"  # Plantilla a utilizar
#     success_url = "/thank-you"  # URL de redirección tras un envío exitoso
#     def form_valid(self, form):
#         form.save()  # Guarda la reseña si el formulario es válido
#         return super().form_valid(form)  # Llama al método padre para continuar con el flujo normal

## 1.3. FORMA MÁS CORTA Y RECOMENDADA UTILIZANDO CreateView
class ReviewView(CreateView):
    model = Review  # Especificamos el modelo a utilizar
    form_class = ReviewForm  # Se usa el formulStudentFormario ReviewForm
    template_name = "reviews/review.html"  # Plantilla a utilizar
    success_url = "/thank-you"  # URL de redirección tras un envío exitoso

## 2. CLASE PARA LA PÁGINA DE AGRADECIMIENTO
class Thank_you_view(TemplateView):
    template_name = "reviews/thank_you.html"  # Plantilla de agradecimiento
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Obtiene el contexto base
        context["message"] = "This works!ʕ·͡ᴥ·ʔ"  # Agrega un mensaje al contexto
        return context

## 3.1. PRIMERA FORMA DE HACER UNA LISTA DE RESEÑAS UTILIZANDO TemplateView
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"  # Plantilla a utilizar
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  # Obtiene el contexto base
#         reviews = Review.objects.all()  # Obtiene todas las reseñas de la base de datos
#         context["reviews"] = reviews  # Agrega las reseñas al contexto
#         return context

## 3.2. FORMA MÁS CORTA UTILIZANDO ListView
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"  # Plantilla a utilizar
    model = Review  # Especificamos el modelo a listar
    context_object_name = "reviews"  # Nombre de la variable que contendrá las reseñas en la plantilla

## 4.1. PRIMERA FORMA DE MOSTRAR UNA SOLA RESEÑA UTILIZANDO TemplateView
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"  # Plantilla a utilizar
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  # Obtiene el contexto base
#         review_id = kwargs["id"]  # Obtiene el ID de la reseña desde la URL
#         selected_review = Review.objects.get(pk=review_id)  # Obtiene la reseña de la base de datos
#         context["review"] = selected_review  # Agrega la reseña al contexto
#         return context

## 4.2. FORMA MÁS CORTA UTILIZANDO DetailView
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"  # Plantilla a utilizar
    model = Review  # Especificamos el modelo a utilizar

### B) VISTA PARA GESTIONAR LAS RESEÑAS SIN UTILIZAR CLASES 
# def review(request):
#     if request.method == 'POST':  # Si la solicitud es POST (se envió un formulario)
#         form = ReviewForm(request.POST)  # Se llena el formulario con los datos enviados
#         if form.is_valid():  # Se verifica si los datos son válidos
#             print(form.cleaned_data)  # Se imprimen los datos limpios (opcional)
#             review = Review(
#                 user_name=form.cleaned_data['user_name'],
#                 review_text=form.cleaned_data['review_text'],
#                 rating=form.cleaned_data['rating']
#             )  # Se crea una instancia de la reseña con los datos del formulario
#             review.save()  # Se guarda la reseña en la base de datos
#             return HttpResponseRedirect("/thank_u")  # Redirige a la página de agradecimiento
#     else:
#         form = ReviewForm()  # Si la solicitud es GET, se crea un formulario vacío
#     return render(request, "reviews/review.html", {"form": form})  # Renderiza la plantilla con el formulario

# # Vista para la página de agradecimiento sin necesidad de lógica adicional
# def thank_u(request):
#     return render(request, "reviews/thank_u.html")  # Renderiza la página de agradecimiento

### STUDENTS VIEWS
class StudentCreateView(CreateView):
    model = Student  # Especificamos el modelo a utilizar
    form_class = StudentForm  # Se usa el formulario StudentForm
    template_name = "students/student_form.html"  # Plantilla a utilizar
    success_url = "/students"  # URL de redirección tras un envío exitoso

class StudentUpdateView(UpdateView):
    model = Student  # Especificamos el modelo a utilizar
    form_class = StudentForm  # Se usa el formulario StudentForm
    template_name = "students/student_form.html"  # Plantilla a utilizar
    success_url = reverse_lazy("students-list")

class StudentDeleteView(DeleteView):
    model = Student  # Especificamos el modelo a utilizar
    template_name = "students/student_confirm_delete.html"  # Plantilla a utilizar
    success_url = reverse_lazy("students-list")


class StudentsListView(ListView):
    template_name = "students/student_list.html"  # Plantilla correcta para estudiantes
    model = Student  # Usamos el modelo Student en vez de Review
    context_object_name = "students"  # Variable correcta en la plantilla
