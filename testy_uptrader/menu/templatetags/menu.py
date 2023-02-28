from django import template
from django.utils.safestring import mark_safe

from menu.models import Menu


register = template.Library()


@register.simple_tag()
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        content = menu.to_html()
        return mark_safe(content)
    except Menu.DoesNotExist:
        return f"Error: Menu with name {menu_name} does not exist"