from django.db import models


class UserRole(models.TextChoices):
    STUDENT = 'student', 'Student'
    TEACHER = 'teacher', 'Teacher'
    SCHOOL_ACCOUNTS = 'school_accounts', 'School Accounts'
    SCHOOL_OFFICE_ASSISTANT = 'school_office_assistant', 'School Office Assistant'
    SCHOOL_ADMIN = 'school_admin', 'School Admin'
    ADMIN = 'admin', 'Admin'
    SUPPORT = 'support', 'Customer Support'


class UserStatus(models.TextChoices):
    Active = 'Active', 'active'
    Inactive = 'Inactive', 'inactive'


class Gender(models.TextChoices):
    FEMALE = "female", "Female"
    MALE = "male", "Male"
    OTHERS = "others", "Others"
