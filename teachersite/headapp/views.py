from multiprocessing import context
from django.shortcuts import get_object_or_404, render
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


def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'headapp/post.html', context=context)


def show_category(request, cat_slug):
    posts = News.objects.filter(cat_slug=cat_slug)
    if len(posts) == 0:
        raise Http404()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'headapp/category.html', context=context)
