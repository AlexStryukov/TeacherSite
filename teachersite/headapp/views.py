from django.shortcuts import render
from django.http import HttpResponse
from headapp.models import *

menu = ["Главная", "Методическая работа", "Достижения", "Обратная связь", "О сайте"]

def index(request):
    posts = News.objects.all()
    return render(request, 'headapp/index.html', {'menu': menu,
                                                  'title': 'Главная страница',
                                                  'posts': posts,
                                                  })
def about(request):
    return render(request, 'headapp/about.html', {'title': 'О сайте',
                                                  'menu': menu,
                                                  })


