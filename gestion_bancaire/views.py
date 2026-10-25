from django.shortcuts import render
from .models import article

# Create your views here.

def home(request):
    users={ 
             
             'nom':'amini', 
             'age':23,
             'sexe': 'M',
             'adresse':'lubumbashi'
             }
    return render(request, 'home.html', users)

def contact(request):
    return render(request, 'contact.html')

def inscription(request):
    return render(request, 'inscription.html')

def service(request):
    return render(request, 'service.html')

def article_list(request):
    articles = article.objects.all()
    return render(request, 'article_list.html', {'articles': articles}) 