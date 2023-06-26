from django import template

register = template.Library()

@register.filter(name='addition')
def addition(value, arg):
    return value+arg
