import logging

from django.conf import settings
from django.urls import reverse

logger = logging.getLogger(__name__)


def get_school_instance(uid):
    from django.core.exceptions import ObjectDoesNotExist
    from .models import SchoolInformationOnBoarding

    try:
        instance = SchoolInformationOnBoarding.objects.get(uid=uid)
        school = instance.id
        return school
    except ObjectDoesNotExist:
        logging.error("This school does not exist")
        return None


def get_base_url():
    """Return the base URL of the server."""
    if settings.DEBUG:
        # If DEBUG is True, use the development server's base URL
        base_url = "http://localhost:8000"
    else:
        # If DEBUG is False, use the production server's base URL
        base_url = reverse("home")

    return base_url
