from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

E2P_NUM = {
    '0': '۰',
    '1': '۱',
    '2': '۲',
    '3': '۳',
    '4': '۴',
    '5': '۵',
    '6': '۶',
    '7': '۷',
    '8': '۸',
    '9': '۹',
}


@register.filter(name='e2p_num')
@stringfilter
def english_number_to_persian_number(value):
    # for e, p in E2P_NUM.items():
    #     if e in value:
    #         value = value.replace(e, p)
    new_value = map(lambda char: E2P_NUM[char] if char in E2P_NUM else char, value)
    return ''.join(list(new_value))
