from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField

from ...models import(
    Student
)

from school_auth.models import (
    User
)

from school_auth.choice import(
    UserRole, UserStatus
)

from StudentApp.choice import(
    Gender,
    BloodGroup,
    Religion,
    MaritalStatus,
    DisabilityStatus,
    EthnicGroup
)

from common.rest.serializers import schoolInformation
from school_auth.rest.serializers import UserSerializer

from common.helpers import get_school_instance

class StudentList(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = [
            "uid",
            'middle_name',
            'gender',
            'date_Of_birth',
            'blood',
            'religion',
            'admission_id',
            'phone',
            'slug',
            'student_name_bangla',
            'student_name_english_captial',
            'birth_certificate_number',
            'birth_of_place',
            'nationality',
            'marital_status',
            'disability_status',
            'ethnic_status',
        ]



class StudentInformationListSerializer(serializers.ModelSerializer):
    basic_info = UserSerializer.UserSerializer(many=False, read_only=True, source='student_user')
    class Meta:
        model = Student
        fields = [
            "basic_info",
            "uid",
            'middle_name',
            'gender',
            'date_Of_birth',
            'blood',
            'religion',
            'admission_id',
            'phone',
            'slug',
            'student_name_bangla',
            'student_name_english_captial',
            'birth_certificate_number',
            'birth_of_place',
            'nationality',
            'marital_status',
            'disability_status',
            'ethnic_status',
        ]