from django.db import models

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from common.models import SchoolInformationOnBoarding
from school_auth.models import User
from core.models import UniversalModel, SchoolClass, SchoolSection

from .choice import (
    Gender,
    BloodGroup,
    Religion,
    FatherStatus,
    MotherStatus,
    MaritalStatus,
    DisabilityStatus,
    EthnicGroup,
    GuardianStatus,
)

from .utills import (
    get_school_student_slug,
    get_student_profile_image,
    get_school_student_image_slug,
    get_school_student_current_slug,
    get_student_permanent_address_slug,
    get_student_present_address_slug,
    # get_student_profile_image_optional,
    # get_student_cover_image_optional,
    # get_student_profile_slug
)


class Student(UniversalModel):
    school_student = models.ForeignKey(
        SchoolInformationOnBoarding,
        on_delete=models.DO_NOTHING,
        related_name="student_school_information",
    )
    student_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="user_student_info",
    )
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        db_index=True,
    )
    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        blank=True,
        null=True,
    )
    date_Of_birth = models.DateField(blank=True, null=True)
    blood = models.CharField(
        max_length=50,
        choices=BloodGroup.choices,
        blank=True,
        null=True,
    )
    religion = models.CharField(
        max_length=50,
        choices=Religion.choices,
        blank=True,
        null=True,
    )
    admission_id = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Phone Number")
    slug = AutoSlugField(
        populate_from=get_school_student_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    student_name_bangla = models.CharField(max_length=255, blank=True, null=True)
    student_name_english_captial = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    birth_certificate_number = models.CharField(max_length=255, blank=True, null=True)
    birth_of_place = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Owen district as follow birth_certificate",
    )
    nationality = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(
        max_length=20,
        choices=MaritalStatus.choices,
        blank=True,
        null=True,
    )
    disability_status = models.CharField(
        max_length=50,
        choices=DisabilityStatus.choices,
        blank=True,
        null=True,
    )
    ethnic_status = models.CharField(
        max_length=50,
        choices=EthnicGroup.choices,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.student_user.username


class StudentImage(UniversalModel):
    student_info = models.ForeignKey(
        Student,
        on_delete=models.DO_NOTHING,
        related_name="student_information",
    )
    slug = AutoSlugField(
        populate_from=get_school_student_image_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    image = VersatileImageField(
        upload_to=get_student_profile_image,
        null=True,
        blank=True,
    )


class StudentCurrentStatus(UniversalModel):
    student_current_status = models.ForeignKey(
        Student,
        on_delete=models.DO_NOTHING,
        related_name="student_current_status_information",
    )
    current_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student_current_class",
    )
    current_section = models.ForeignKey(
        SchoolSection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="student_current_section",
    )
    slug = AutoSlugField(
        populate_from=get_school_student_current_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    class_roll_number = models.CharField(max_length=100, blank=True, null=True)


class StudentPermanentAddress(UniversalModel):
    student_permanent_address = models.ForeignKey(
        Student,
        on_delete=models.DO_NOTHING,
        related_name="student_permanent_address_information",
    )
    slug = AutoSlugField(
        populate_from=get_student_permanent_address_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    divisions = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    upazila = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Upozila or Thana",
    )
    pourashava = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Pourashava or City Corporation",
    )
    union_parishad = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    mouza = models.CharField(max_length=255, blank=True, null=True)
    village = models.TextField(
        max_length=555,
        blank=True,
        null=True,
        verbose_name="Rasta/village",
    )
    house_holding_number = models.CharField(max_length=255, blank=True, null=True)
    post_office = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)


class StudentPresentAddress(UniversalModel):
    student_present_address = models.ForeignKey(
        Student,
        on_delete=models.DO_NOTHING,
        related_name="student_present_address_information",
    )
    slug = AutoSlugField(
        populate_from=get_student_present_address_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    divisions = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    upazila = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Upozila or Thana",
    )
    pourashava = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Pourashava or City Corporation",
    )
    union_parishad = models.CharField(max_length=255, blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    mouza = models.CharField(max_length=255, blank=True, null=True)
    village = models.TextField(
        max_length=555,
        blank=True,
        null=True,
        verbose_name="Rasta/village",
    )
    house_holding_number = models.CharField(max_length=255, blank=True, null=True)
    post_office = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)


class StudentFather(UniversalModel):
    student_father = models.ForeignKey(
        Student,
        on_delete=models.DO_NOTHING,
        related_name="student_father_information",
    )
    name_bangla = models.CharField(max_length=255, blank=True, null=True)
    name_english_capital = models.CharField(max_length=255, blank=True, null=True)
    nid = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    birth_certificate_number = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Phone Number")
    occupation = models.CharField(max_length=255, blank=True, null=True)
    father_status = models.CharField(
        max_length=20,
        choices=FatherStatus.choices,
        blank=True,
        null=True,
    )
    date_of_death = models.DateField(blank=True, null=True)


class StudentMother(UniversalModel):
    student_mother = models.ForeignKey(
        Student, on_delete=models.DO_NOTHING, related_name="student_mother_information"
    )
    name_bangla = models.CharField(max_length=255, blank=True, null=True)
    name_english_capital = models.CharField(max_length=255, blank=True, null=True)
    nid = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    birth_certificate_number = models.CharField(max_length=255, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Phone Number")
    occupation = models.CharField(max_length=255, blank=True, null=True)
    mother_status = models.CharField(
        max_length=20,
        choices=MotherStatus.choices,
        blank=True,
        null=True,
    )
    date_of_death = models.DateField(blank=True, null=True)


class StudentGuardian(UniversalModel):
    # "if student parents both die then applicable"
    name = models.CharField(max_length=255, blank=True, null=True)
    nid = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    guardian_status = models.CharField(
        max_length=20,
        choices=GuardianStatus.choices,
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Phone Number")
