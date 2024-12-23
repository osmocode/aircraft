from django import template

register = template.Library()

@register.filter(name='append_class')
def append_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    # check if class is set or empty and split its content to list (or init list)
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    # prepare new classes to list
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    # join back to single string
    return value.as_widget(attrs={'class': ' '.join(css_classes)})