from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from headapp.models import *
from headapp.forms import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Методическая работа", 'url_name': 'method_work'},
        {'title': "Достижения", 'url_name': 'achievements'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
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


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Добавление статьи',
    }
    return render(request, 'headapp/addpage.html', context=context)


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
    cat_id = get_object_or_404(Category, slug=cat_slug).pk
    posts = News.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'posts': posts,
        'cat_selected': cat_id,
    }
    return render(request, 'headapp/category.html', context=context)
