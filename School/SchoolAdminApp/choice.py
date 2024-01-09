from django.db import models


class Gender(models.TextChoices):
    FEMALE = "female", "Female"
    MALE = "male", "Male"
    OTHERS = "others", "Others"



class JobType(models.TextChoices):
    FullTime = 'full_time', 'Full Time'
    PartTime = 'part_time', 'Part Time'
    Internship = 'internship', 'Internship'
    Temporary = 'temporary', 'Temporary'
    Remote = 'remote', 'Remote'
    Other = 'other', "Other"



class JobStatus(models.TextChoices):
    Open = 'open', 'Open'
    Closed = 'closed', 'Closed'
    Cancelled = 'cancelled', 'Cancelled'