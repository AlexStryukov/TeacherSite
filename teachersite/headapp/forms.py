from email.policy import default
from unicodedata import name
from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок")
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        label="Содержимое статьи")
    is_published = forms.BooleanField(label="Опубликовать")
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(), label="Категория")
