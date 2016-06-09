# templatetags/nbsp.py

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='nbsp')
def nbsp(value):
    return mark_safe("&nbsp;".join(value.split(' ')))

@register.filter(name='times')
def times(number):
    return range(number)

@register.filter(name='br')
def br(value):
    return mark_safe("<br>".join(value.split('\n')))
