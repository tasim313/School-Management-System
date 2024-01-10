from uuid import uuid4
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_school_admin_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-admin'}-{str(instance.uid).split('-')[0]}"


def get_school_admin_image_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}-{str(instance.uid).split('-')[0]}"



def get_admin_profile_image(instance, filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}-{timestamp}-{filename}"



def get_school_career_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-career'}-{str(instance.uid).split('-')[0]}"


def get_school_library_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-library'}-{str(instance.uid).split('-')[0]}"


def get_school_transport_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-transport'}-{str(instance.uid).split('-')[0]}"