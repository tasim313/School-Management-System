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
    Gender
)

from .utills import(
    get_school_admin_slug,
    get_school_admin_image_slug,
    get_admin_profile_image
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