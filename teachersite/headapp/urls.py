from django.urls import path

from headapp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('method_work/', method_work, name='method_work'),
    path('achievements', achievements, name='achievements'),
    path('feedback', feedback, name='feedback'),
    path('post/<int:post_id>/', show_post, name='posts')
]