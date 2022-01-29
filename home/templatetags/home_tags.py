from django import template
from home.models import AboutUs


register = template.Library()

@register.inclusion_tag('home/tags/aboutUs.html', takes_context=True)
def aboutUs(context):
    return {
        'aboutUs': AboutUs.objects.all(),
        'request': context['request'],
    }