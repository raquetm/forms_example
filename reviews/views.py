from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.
def review(request):
    if request.method=='POST':
            form =ReviewForm(request.POST)

            if form.is_valid():
                print(form.cleaned_data)
                review = Review(
                    user_name=form.cleaned_data['user_name'],
                    review_text=form.cleaned_data['review_text'],
                    rating=form.cleaned_data['rating']

                )
                review.save()
                return HttpResponseRedirect("/thank_u")
            
    else:
        form =ReviewForm()
    #Enviámoslle o formulario á plantilla review
    #Se o usuario enviou datos ese form vai ter os datos
    #Si se carga a páxina por primeira vez ese form está baleiro
    return render(request, "reviews/review.html", {"form":form})

def thank_u(request):
    return render(request, "reviews/thank_u.html")