from django.db import models

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from common.models import  SchoolInformationOnBoarding
from school_auth.models import User

from core.models import (
    UniversalModel,
    SchoolClass, 
    SchoolSection)


from .choice import (
    Gender,
    JobType,
    JobStatus,
    BookType,
    BookStatus,
    HostelRoomType,
    HostelAvailability,
)

from .utills import(
    get_school_admin_slug,
    get_school_admin_image_slug,
    get_admin_profile_image,
    get_school_career_slug,
    get_school_library_slug,
    get_school_transport_slug
)


class SchoolAdmin(UniversalModel):
    school_admin = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_admin_information')
    schoolUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_school_admin_info')
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        blank=True, null=True
    )
    date_Of_birth = models.DateField(blank=True, null=True)
    phone =  PhoneNumberField(blank=True, null=True, verbose_name='Phone Number')
    joining_date  = models.DateTimeField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    slug = AutoSlugField(populate_from=get_school_admin_slug, unique=True, null=False, db_index=True)

   
    def __str__(self):
        return self.schoolUser.username
    
    

class SchoolAdminImage(UniversalModel):
    school_admin_info = models.ForeignKey(SchoolAdmin, on_delete=models.DO_NOTHING, related_name='school_admin_information')
    slug = AutoSlugField(populate_from=get_school_admin_image_slug, unique=True, null=False, db_index=True)
    image = VersatileImageField(upload_to=get_admin_profile_image, null=True, blank=True)




class Department(UniversalModel):
    school_department = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_departments')
    department_id = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=500, blank=True, null=True)
    head_of_department = models.CharField(max_length=500, blank=True, null=True)



class Career(UniversalModel):
    school_career = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_job_circular')
    career_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="job_department")
    title = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=550, blank=True, null=True)
    experience = models.TextField(max_length=1000, blank=True, null=True)
    no_of_vacancies = models.CharField(max_length=100, blank=True, null=True)
    age_limit = models.CharField(max_length=100, blank=True, null=True)
    salary_from = models.CharField(max_length=255, blank=True, null=True)
    salary_to = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(
        max_length=50,
        choices=JobType.choices,
        blank=True, null=True
    )
    job_status = models.CharField(
        max_length=30,
        choices=JobStatus.choices,
        blank=True, null=True
    )
    start_date = models.DateTimeField(blank=True, null=True)
    expired_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    slug = AutoSlugField(populate_from=get_school_career_slug, unique=True, null=False, db_index=True)

    class Meta:
        ordering = ["-createdAt"]
        verbose_name_plural = "Career"



class Library(UniversalModel):
    school_library = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_libraries')
    library_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="library_departments")
    library_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="library_classes")
    slug = AutoSlugField(populate_from=get_school_library_slug, unique=True, null=False, db_index=True)
    book_id = models.CharField(max_length=100, unique=False)
    book_name = models.CharField(max_length=500, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    book_type = models.CharField(
        max_length=30,
        choices=BookType.choices,
        blank=True, null=True
    )
    book_status = models.CharField(
        max_length=30,
        choices=BookStatus.choices,
        blank=True, null=True
    )
    


class Transport(UniversalModel):
    school_transport = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_transports')
    slug = AutoSlugField(populate_from=get_school_transport_slug, unique=True, null=False, db_index=True)
    route_name =  models.CharField(max_length=500, blank=True, null=True)
    vehicle_number = models.CharField(max_length=500, blank=True, null=True)
    driver_name = models.CharField(max_length=500, blank=True, null=True)
    license_number = models.CharField(max_length=500, blank=True, null=True)
    contact_number = models.CharField(max_length=500, blank=True, null=True)
    driver_address = models.TextField(blank=True, null=True)



class Hostel(UniversalModel):
    school_hostel = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_hostel')
    block = models.CharField(max_length=255, blank=True, null=True)
    room_number = models.CharField(max_length=255, blank=True, null=True)
    room_type = models.CharField(
        max_length=30,
        choices=HostelRoomType.choices,
        blank=True, null=True
    )
    number_of_beds = models.CharField(max_length=100, blank=True, null=True)
    cose_per_bed = models.CharField(max_length=100, blank=True, null=True)
    availability = models.CharField(
        max_length=30,
        choices=HostelAvailability.choices,
        blank=True, null=True
    )


class SportsInformation(UniversalModel):
    school_sports = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_sports')
    sports_id = models.CharField(max_length=100, unique=False)
    sports_name = models.CharField(max_length=255, blank=True, null=True)
    coach_name = models.CharField(max_length=255, blank=True, null=True)
    started_year = models.CharField(max_length=255, blank=True, null=True)



class ClassTimeTable(UniversalModel):
    school_class_time_table = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_class_time_table')
    school_time_table = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='school_class_information')
    school_section_time_table = models.ForeignKey(SchoolSection, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='school_section_information')
    teacher_id = models.CharField(max_length=100, unique=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    class_date = models.DateTimeField(blank=True, null=True)
    class_start_time = models.TimeField(blank=True, null=True)
    class_end_time = models.TimeField(blank=True, null=True)


class Exam(UniversalModel):
    school_exam = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='school_exams')
    exam_class = models.ForeignKey(SchoolClass, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='exam_classes')
    exam_section = models.ForeignKey(SchoolSection, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='exam_sections')
    name = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    fees = models.CharField(max_length=255, blank=True, null=True)
    exam_start_time = models.TimeField(blank=True, null=True)
    exam_end_time = models.TimeField(blank=True, null=True)
    exam_date = models.DateTimeField(blank=True, null=True)