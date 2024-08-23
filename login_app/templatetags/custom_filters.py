from django import template

register = template.Library()

@register.filter
def get_color(colors, index):
    color_keys = list(colors.keys())
    color_index = index % len(color_keys)
    return colors[color_keys[color_index]]