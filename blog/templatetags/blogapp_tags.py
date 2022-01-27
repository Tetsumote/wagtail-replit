from blog.models import BlogPage
from django.template import Library, loader

register = Library()

@register.inclusion_tag('blog/components/posts_list.html',
takes_context=True)
def posts_list(context):
  posts = BlogPage.objects.all()[:3]
  return {
  'request': context['request'],
  'posts': posts
  }
