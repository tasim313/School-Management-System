from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


def get_website_information_instance(uid):
    from django.core.exceptions import ObjectDoesNotExist
    from .models import WebsiteInformation

    try:
        instance = WebsiteInformation.objects.get(uid=uid)
        website = instance.id
        return website
    except ObjectDoesNotExist:
        logging.error("This website information does not exist")
        return None
    

def get_website_about(uid):
    from django.core.exceptions import ObjectDoesNotExist
    from .models import WebsiteAbout

    try:
        instance = WebsiteAbout.objects.get(uid=uid)
        about = instance.id
        return about
    except ObjectDoesNotExist:
        logging.error("This website  about information does not exist")
        return None