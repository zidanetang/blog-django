from office_blog.models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count


register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_archives():
    archives_list = Post.objects.dates('created_time','month',order='DESC').annotate()
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_category():
    category_list = Category.objects.annotate(num_posts=Count('post'))
    return category_list

@register.simple_tag
def get_tags(num=10):
    return Tag.objects.all()[:num]
