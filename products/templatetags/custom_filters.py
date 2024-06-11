from django import template

register = template.Library()

@register.filter
def range(start, end):
    return range(start, end)
