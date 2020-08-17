from django import template

register = template.Library()


@register.inclusion_tag('itcase_rotator/rotator.html', takes_context=True)
def category_rotator(context, category, additional_class=None,
                     autoplay=None, loop=True):
    context['rotator'] = category.rotator_units.all()
    if additional_class:
        context['additional_class'] = additional_class
    context['autoplay'] = autoplay
    context['loop'] = loop
    return context.flatten()
