from django import template

register = template.Library()


@register.filter(name='check_odds')
def check_odds(odds, bet):
    return odds[bet]
