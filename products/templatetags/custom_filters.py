from django import template

register = template.Library()

@register.filter
def to_range(value):
    """Converts an integer to a range for iteration in templates."""
    return range(1, value)
