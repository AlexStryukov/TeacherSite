from django.shortcuts import render
from django.http import HttpResponse, Http404
from headapp.models import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Методическая работа", 'url_name': 'method_work'},
        {'title': "Достижения", 'url_name': 'achievements'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
        {'title': "О сайте", 'url_name': 'about'}]

def index(request):
    posts = News.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': 0,
    }


    return render(request, 'headapp/index.html', context=context)
def about(request):
    return render(request, 'headapp/about.html', {'title': 'О сайте',
                                                  'menu': menu,
                                                  })
def method_work(request):
    return HttpResponse('Методическая работа')
def achievements(request):
    return HttpResponse('Достижения')
def feedback(request):
    return HttpResponse('Обратная связь')
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с ID = {post_id}")
def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    if len(posts)==0:
        raise Http404()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'headapp/category.html', context=context)

