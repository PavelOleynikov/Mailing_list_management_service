from django import template

register = template.Library()


@register.filter()
def split_fullname(fullname):
    parts = str(fullname).split(" ")
    last_name = parts[0]
    initials = [part[0].upper() + "." for part in parts[1:]]
    return f"{last_name} {' '.join(initials)}"
