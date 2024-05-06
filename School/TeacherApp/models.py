from django.db import models

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField
from django.db.models.signals import post_save

from common.models import  SchoolInformationOnBoarding
from school_auth.models import User


from core.models import (
    UniversalModel,
    SchoolClass, 
    SchoolSection)

from .choice import (
    Gender
)

from .utills import(
    get_school_teacher_slug,
    get_school_teacher_image_slug,
    get_teacher_profile_image
)


class Teacher(UniversalModel):
    school_teacher = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.DO_NOTHING, related_name='teacher_school_information')
    teacher_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_teacher_info')
    teacher_id = models.CharField(max_length=255, blank=True, null=True)
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
    slug = AutoSlugField(populate_from=get_school_teacher_slug, unique=True, null=False, db_index=True)
    

    def __str__(self):
        return self.teacher_user.username
    



class TeacherImage(UniversalModel):
    teacher_info = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name='teacher_information')
    slug = AutoSlugField(populate_from=get_school_teacher_image_slug, unique=True, null=False, db_index=True)
    image = VersatileImageField(upload_to=get_teacher_profile_image, null=True, blank=True)


def create_teacher_image(sender, instance, created, **kwargs):
        TeacherImage.objects.create(teacher_info=instance)
post_save.connect(create_teacher_image, sender=Teacher)