from django import template
from jalali_date import datetime2jalali

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
	return value.replace(arg, '')


@register.filter(name='show_jalal')
def show_jalali(value):
	return datetime2jalali(value)

@register.filter(name='uppercase')
def uppercase(value: str):
	return value.capitalize()