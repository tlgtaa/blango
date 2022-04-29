from typing import Optional

from django.contrib.auth import get_user_model
from django.template import Library
from django.utils.html import format_html
from django.utils.safestring import mark_safe

User = get_user_model()
register = Library()


@register.filter
def author_details(author: Optional[User], current_user):
  if not isinstance(author, User):
    return ''

  if author == current_user:
    return format_html('<strong>me</strong>')

  name = author.username
  if all([author.first_name, author.last_name]):
    name = f'{author.first_name} {author.last_name}'
  
  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html('</a>')
  else:
    prefix = ''
    suffix = ''

  return format_html('{}{}{}', prefix, name, suffix)
