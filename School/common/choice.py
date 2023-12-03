from django.db import models


class SchoolType(models.TextChoices):
    SMALL = 'S', '100 to 500 students'
    MEDIUM = 'M', '100 to 1000 students'
    LARGE = 'L', '100 to 2000 students'
    XLARGE = 'XL', '100 to 3000 students'
    XXLARGE = 'XXL', '100 to 5000 students'

class Status(models.TextChoices):
    Active = 'Active', 'active'
    Inactive = 'Inactive', 'inactive'

