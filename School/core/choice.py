from django.db import models


class Status(models.TextChoices):
    Active = 'Active', 'active'
    Inactive = 'Inactive', 'inactive'



class AdmissionClass(models.TextChoices):
    CLASS_ONE = 'class_one', 'Class One'
    CLASS_TWO = 'class_two', 'Class Two'
    CLASS_THREE = 'class_three', 'Class Three'
    CLASS_FOUR = 'class_four', 'Class Four'
    CLASS_FIVE = 'class_five', 'Class Five'
    CLASS_SIX = 'class_six', 'Class Six'
    CLASS_SEVEN = 'class_seven', 'Class Seven'
    CLASS_EIGHT = 'class_eight', 'Class Eight'
    CLASS_NINE = 'class_nine', 'Class Nine'
    CLASS_TEN = 'class_ten', 'Class Ten'
    CLASS_ELEVEN = 'class_eleven', 'Class Eleven'
    CLASS_TWELVE = 'class_twelve', 'Class Twelve'


class AdmissionBranch(models.TextChoices):
    PRABHATI = 'prabhati', 'প্রভাতী'
    DIBA = 'diba', 'দিবা'
    NO_BRANCH = 'no_branch', 'কোন শাখা নেই'

class AdmissionDivision(models.TextChoices):
    BANGLA = 'bangla', 'বাংলা'
    ENGLISH = 'english', 'ইংরেজি'