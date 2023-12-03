from uuid import uuid4
import logging

logger = logging.getLogger(__name__)



def get_school_info_onboard_slug(instance):
    return (f"{str(instance.name)}{str(instance.uid).split('-')[0]}")
