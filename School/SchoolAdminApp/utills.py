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



def get_school_vendor_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-vendor'}-{str(instance.uid).split('-')[0]}"


def get_school_product_category_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-product-category'}-{str(instance.uid).split('-')[0]}"


def get_school_product_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-product'}-{str(instance.uid).split('-')[0]}"


def get_school_purchase_request_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-purchase-request'}-{str(instance.uid).split('-')[0]}"


def get_school_purchase_received_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-purchase-received'}-{str(instance.uid).split('-')[0]}"


def get_school_hostel_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-hostel'}-{str(instance.uid).split('-')[0]}"


def get_school_sports_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-sports'}-{str(instance.uid).split('-')[0]}"


def get_school_class_time_table_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-class-time-table'}-{str(instance.uid).split('-')[0]}"


def get_school_exam_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-exam'}-{str(instance.uid).split('-')[0]}"


def get_school_grading_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-grading'}-{str(instance.uid).split('-')[0]}"


def get_school_semester_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-semester'}-{str(instance.uid).split('-')[0]}"


def get_school_holiday_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-holiday'}-{str(instance.uid).split('-')[0]}"


def get_curriculum_vitae_file(instance, filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    uid = str(uuid4()).split("-")[-1]
    return f"{'Candidate'}{uid}{'cv'}{timestamp}-{filename}"


def get_employee_candidate_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'employee-candidate'}-{str(instance.uid).split('-')[0]}"