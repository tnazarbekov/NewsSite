from django import template
from django.db.models import Count
from news.models import *
from django.db.models import F
register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='hello', arg2='world'):
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=-1)
    categories = Category.objects.annotate(cnt=Count('news',filter=F('news__is_published'))).filter(cnt__gt=-1)
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}
