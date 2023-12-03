from uuid import uuid4
from datetime import datetime
import logging

logger = logging.getLogger(__name__)



def get_school_student_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'student'}-{str(instance.uid).split('-')[0]}"

logger.debug(f"get_school_student_slug: {get_school_student_slug}")


def get_student_profile_image(instance, filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}-{timestamp}-{filename}"

logger.debug(f"get_student_profile_image: {get_student_profile_image}")



def get_school_student_image_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}-{str(instance.uid).split('-')[0]}"

logger.debug(f"get_school_student_image_slug: {get_school_student_image_slug}")



def get_school_student_current_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return (f"{uid}{'school-student'}{str(instance.uid).split('-')[0]}")

logger.debug(f"get_school_student_current_slug: {get_school_student_current_slug}")


def get_student_permanent_address_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return (f"{uid}{'student-address-permanent'}{str(instance.uid).split('-')[0]}")


def get_student_present_address_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return (f"{uid}{{'student-present-address'}}{str(instance.uid).split('-')[0]}")


def get_student_profile_image_optional(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image-optional'}-{filename}"


def get_student_cover_image_optional(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image-optional'}-{filename}"


# def get_student_profile_slug(instance):
#     uid = str(uuid4()).split("-")[-1]
#     return (f"{uid}{'student-profile'}{str(instance.uid).split('-')[0]}")