from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission
    )


from common.models import(
    SchoolInformationOnBoarding
)

from .choice import (
    UserRole,
    UserStatus
)



import logging

logger = logging.getLogger(__name__)




class CustomUserManager(BaseUserManager):

    def create_user(self, username=None, password=None, role=None, **extra_fields):
        if not username:
            raise ValueError('Users must have username')

        if not role:
            raise ValueError('Users must have a role')

        user = self.model(username=username, role=role, **extra_fields)

        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, username,  password=None, **extra_fields):
        """
        Create and return a superuser with username, role='Admin', and password.
        """
        extra_fields.setdefault('role', 'Admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username=username, password=password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='school_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='school_user_permissions')
    school = models.ForeignKey(SchoolInformationOnBoarding, on_delete=models.CASCADE, blank=True, null=True, related_name="on_board_school_user")
    email = models.EmailField(
        unique=True,
        verbose_name='user email address',
        max_length=255,
        blank=True,
        null=True,
    )

    username = models.CharField(max_length=255, unique=True, verbose_name='User ID')

    role = models.CharField(
        max_length=30,
        choices=UserRole.choices,
        default= UserRole.SUPPORT
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.Active
    )

    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255, blank=False, null=False)

    
    USERNAME_FIELD = 'username'


    REQUIRED_FIELDS = ['role', 'firstName', 'lastName' ]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def save(self, *args, **kwargs):
        self.username = self.username
        return super().save(*args, **kwargs)