from uuid import uuid4
import logging

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
