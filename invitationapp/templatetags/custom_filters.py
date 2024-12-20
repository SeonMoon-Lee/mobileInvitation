# myapp/templatetags/custom_filters.templatetags
from datetime import datetime

from django import template

register = template.Library()


@register.filter
def korean_weekday(date):
    days = ["월", "화", "수", "목", "금", "토", "일"]
    return days[date.weekday()]


@register.filter
def english_weekday(value):
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%Y-%m-%d')  # 문자열을 datetime으로 변환
        except ValueError:
            return value  # 변환 실패 시 원래 문자열 반환
    return value.strftime('%A')  # 요일 이름 반환
