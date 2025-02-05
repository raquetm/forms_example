from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

class ReviewView(CreateView):
    Model=Review
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url="/thank-you"


# class ReviewView(FormView):
#     form_class=ReviewForm
#     template_name="reviews/review.html"
#     success_url="/thank-you"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

class Thank_you_view(TemplateView):
    template_name="reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["message"]="This works!"
        return context

class ReviewsListView(ListView):
    template_name="reviews/review_list.html"
    model=Review
    context_object_name="reviews"

# class ReviewsListView(TemplateView):
#     template_name="reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context["reviews"]=reviews
#         return context
class SingleReviewView(DetailView):
    template_name="reviews/single_review.html"
    model =Review

# class SingleReviewView(TemplateView):
#     template_name="reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         review_id=kwargs["id"]
#         selected_review=Review.objects.get(pk=review_id)
#         context["review"]=selected_review
#         return context

# # Vista para gestionar las reseñas
# def review(request):
#     # Verificamos si la solicitud es de tipo POST (cuando el usuario envía el formulario)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)  # Creamos una instancia del formulario con los datos enviados

#         if form.is_valid():  # Verificamos si los datos son válidos según las reglas del formulario
#             print(form.cleaned_data)  # Imprimimos los datos validados en la consola (opcional)

#             # Creamos una nueva instancia del modelo Review con los datos del formulario
#             review = Review(
#                 user_name=form.cleaned_data['user_name'],
#                 review_text=form.cleaned_data['review_text'],
#                 rating=form.cleaned_data['rating']
#             )
#             review.save()  # Guardamos la reseña en la base de datos

#             # Redirigimos al usuario a la página de agradecimiento
#             return HttpResponseRedirect("/thank_u")

#     else:
#         # Si la solicitud es GET (es decir, el usuario solo abre la página), mostramos un formulario vacío
#         form = ReviewForm()
    
#     #Enviámoslle o formulario á plantilla review
#     #Se o usuario enviou datos ese form vai ter os datos
#     #Si se carga a páxina por primeira vez ese form está baleiro
#     # Renderizamos la plantilla 'review.html' enviando el formulario al contexto
#     return render(request, "reviews/review.html", {"form": form})

# # Vista para la página de agradecimiento
# def thank_u(request):
#     # Renderizamos la plantilla 'thank_u.html' sin necesidad de enviar datos adicionales
#     return render(request, "reviews/thank_u.html")
