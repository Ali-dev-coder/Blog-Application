import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import  mark_safe

register = template.Library()
@register.filter
def convert_markdown(value):
    return markdown.markdown(value)