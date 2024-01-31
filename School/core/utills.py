import os

from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


def get_school_class_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-class'}{str(instance.uid).split('-')[0]}"


def get_school_section_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-section'}{str(instance.uid).split('-')[0]}"


def get_school_address_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-address'}{str(instance.uid).split('-')[0]}"


def get_school_website_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-website'}-{str(instance.uid).split('-')[0]}"


def get_school_contact_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-contact'}{str(instance.uid).split('-')[0]}"


def get_website_home_slider_content_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'slider'}{'content'}{str(instance.uid).split('-')[0]}"


def get_website_home_slider_content_file_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'slider'}{'file'}{str(instance.uid).split('-')[0]}"


def get_website_about_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'about'}{str(instance.uid).split('-')[0]}"


def get_website_about_file_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'about-file'}{str(instance.uid).split('-')[0]}"


def get_website_school_admission_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'admission'}{str(instance.uid).split('-')[0]}"


def get_website_school_academic_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'academic'}{str(instance.uid).split('-')[0]}"


def get_school_website_logo(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'website-logo'}-{filename}-{str(instance.uid).split('-')[0]}"


def get_school_website_favicon(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'website-favicon'}-{filename}-{str(instance.uid).split('-')[0]}"


def get_website_home_slider_content_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_website_about_file_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_website_about_file_awards_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_website_about_file_awards_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_website_school_admission_pdf(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'school-admission-pdf'}{'admission'}-{filename}{str(instance.uid).split('-')[0]}"


def get_website_school_academic_homework_and_lecture_documents_pdf(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'homework-lecture-pdf'}{'document'}-{filename}{str(instance.uid).split('-')[0]}"


def get_website_school_academic_lesson_plan_documents_pdf(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'lesson-plan-pdf'}{'document'}-{filename}{str(instance.uid).split('-')[0]}"


def get_website_school_academic_calendar_documents_pdf(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'academic-calender-pdf'}{'document'}-{filename}{str(instance.uid).split('-')[0]}"


def get_website_school_academic_syllabus_documents_pdf(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'academic-calender-pdf'}{'document'}-{filename}{str(instance.uid).split('-')[0]}"


def get_website_school_academic_class_routine_documents_pdf(instance, filename):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'class-routine-pdf'}{'document'}-{filename}{str(instance.uid).split('-')[0]}"


def get_website_get_gallery_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_blog_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_news_events_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'news-events'}{str(instance.uid).split('-')[0]}"


def get_news_events_image(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"


def get_blog_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'blog'}{str(instance.uid).split('-')[0]}"

def get_blog_image_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'blog'}{str(instance.uid).split('-')[0]}"


def get_social_media_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'social-media'}{str(instance.school_social_media_website_information.uid).split('-')[0]}"


def get_alumni_section_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'alumni-section'}{str(instance.school_alumni_section_website_information.uid).split('-')[0]}"


def get_website_teacher_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'website-teacher'}{str(instance.uid).split('-')[0]}"


def get_website_managing_committee_member_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'managing_committee_member'}{str(instance.uid).split('-')[0]}"


def get_website_staff_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'website-staff'}{str(instance.uid).split('-')[0]}"


def get_website_faculty_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'website-staff'}{str(instance.uid).split('-')[0]}"




def get_testimonials_image(instance, filename):
    clean_filename = os.path.basename(filename)  
    return f"image/{instance.uid}/{clean_filename}"


def get_testimonials_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'testimonials'}{str(instance.uid).split('-')[0]}"


def get_alumni_section_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'alumni'}{str(instance.uid).split('-')[0]}"

def get_alumni_section_image_slug(instance):
    uid = str(uuid4()).split("-")[-1]
    return f"{uid}{'alumni'}{str(instance.uid).split('-')[0]}"