from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def multiply(value, arg):
    print('test: ')
    print(arg)
    return float(value) * float(arg)

@register.filter
def seconds(value):
    return value.seconds

@register.filter
def divide(value, arg):
    return value / int(arg)

@register.filter
def days(value):
    return value.days

@register.filter
def hours(value):
    hours = str(int(value / 3600))
    if len(hours) < 2:
        hours = '0' + hours
    return(hours)

@register.filter
def minutes(value):
    minutes = str(int(((value % 3600))/ 60))
    if len(minutes) < 2:
        minutes = '0' + minutes
    return(minutes)

@register.filter
def seconds_simple(value):
    seconds = str(int((value % 3600) % 60))
    if len(seconds) < 2:
        seconds = '0' + seconds
    return(seconds)

@register.filter
def last_4(value):
    length = len(value)
    if length >= 4:
        start = length-4
        last = value[start:]
    else:
        last = value
    return(last)

@register.filter
def print(value):
    print(value)
    return(value)