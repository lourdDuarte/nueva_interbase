from atexit import register
from os import remove
from django import template
from pymysql import NULL

register = template.Library()

@register.filter()
def comas(value):
    if value:
        return value.replace(',','.')

@register.filter()
def fame(value):
    if value == 'F':
        return value.replace('F','femenino')
    

