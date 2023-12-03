from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from ...models import(
    Student
)

from common.rest.serializers import schoolInformation
from school_auth.rest.serializers import UserSerializer



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
