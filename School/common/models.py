from django.db import models

import uuid


from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField


from .utills import (
    get_school_info_onboard_slug,
)

from .choice import (
    SchoolType,
)


class BaseModel(models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)


class SchoolInformationOnBoarding(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.TextField(max_length=550, blank=False, null=False)
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Phone Number")
    slug = AutoSlugField(
        populate_from=get_school_info_onboard_slug,
        unique=True,
        null=False,
        db_index=True,
    )
    school_type = models.CharField(max_length=3, choices=SchoolType.choices)
    username = models.CharField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        # If the username is not set, generate a unique username
        if not self.username:
            self.username = self.generate_unique_username()
        # Call the super method to save the model
        super(SchoolInformationOnBoarding, self).save(*args, **kwargs)

    def generate_unique_username(self):
        # Convert the name to lowercase and remove spaces
        base_user_name = self.name.lower().replace(" ", "")
        # Generate a random string as a unique identifier
        unique_part = str(uuid.uuid4().hex)[:6]
        # Combine the base username and unique part to form the unique username
        return f"{base_user_name}{unique_part}"

    def __str__(self):
        return self.name
