from django.urls import path

from headapp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('method_work/', method_work, name='method_work'),
    path('achievements/', achievements, name='achievements'),
    path('feedback/', feedback, name='feedback'),
    path('post/<slug:post_slug>/', show_post, name='posts'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
]
