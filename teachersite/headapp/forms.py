from dataclasses import field
from email.policy import default
from re import S
from unicodedata import name
from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = News
        fields = ["title", "slug", 'content', 'is_published', 'cat']
        widget = {
            'title': forms.TextInput(attrs={'class': 'form_input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'cat': forms.ChoiceField()
        }
