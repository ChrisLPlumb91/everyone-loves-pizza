from django import template


register = template.Library()


@register.filter(name='replace_spaces')
def replace_spaces(string):

    new_string = string.replace(' ', '-')

    return new_string
