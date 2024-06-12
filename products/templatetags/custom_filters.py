# custom_filters.py in your templatetags directory
from django import template

register = template.Library()

@register.filter(name='to_range')
def to_range(value):
    return range(1, value + 1)
