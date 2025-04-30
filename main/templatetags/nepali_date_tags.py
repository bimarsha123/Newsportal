# my_app/templatetags/nepali_date_tags.py
from django import template
import nepali_datetime
from django.utils import timezone

register = template.Library()

@register.filter(name="nepali_date")
def to_nepali_date(value):
    """Converts English datetime to Nepali date."""
    if not value:
        value = timezone.now()
    return nepali_datetime.datetime.now().strftime("%B %d, %Y")
