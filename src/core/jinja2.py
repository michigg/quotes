from django.templatetags.static import static
from django.urls import reverse
from django.conf import settings

from jinja2 import Environment

from core.version import VERSION_TAG


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'site_name': settings.SITE_NAME,
        'version': VERSION_TAG
    })
    return env
