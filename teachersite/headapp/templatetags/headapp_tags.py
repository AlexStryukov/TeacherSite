from django import template
from headapp.models import *

register = template.Library()

@register.simple_tag(name="getcats")
def get_categories():
    return Category.objects.all()