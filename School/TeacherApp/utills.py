from uuid import uuid4
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def get_school_teacher_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'teacher'}-{str(instance.uid).split('-')[0]}"


def get_school_teacher_image_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}-{str(instance.uid).split('-')[0]}"

logger.debug(f"get_school_student_image_slug: {get_school_teacher_image_slug}")


def get_teacher_profile_image(instance, filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'image'}-{timestamp}-{filename}"

logger.debug(f"get_student_profile_image: {get_teacher_profile_image}")

