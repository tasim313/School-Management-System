from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField

from ...models import User

from ...choice import UserRole, UserStatus


from common.helpers import get_school_instance


from StudentApp.choice import(
    Gender,
    BloodGroup,
    Religion,
    MaritalStatus,
    DisabilityStatus,
    EthnicGroup
)

from StudentApp.models import(
    Student
)

from SchoolAdminApp.models import SchoolAdmin
from SchoolAdminApp.choice import(
    Gender
)

from StudentApp.rest.serializers import student
from school_auth.rest.serializers import UserSerializer

import logging

logger = logging.getLogger(__name__)



class RegisterSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    email = serializers.EmailField(
            required=False,
            label="Email",
            allow_blank=True,
            validators=[UniqueValidator(queryset=User.objects.all())],
            )
    firstName = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="Student First Name")
    lastName = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="Student Last Name")
    username = serializers.CharField(
        max_length=255, 
        required=True, allow_blank=False, validators=[UniqueValidator(queryset=User.objects.all())],label="User Name or User ID or Email")
    
    role = serializers.ChoiceField(
           label="User Role",
           choices = UserRole.choices
    )

    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=False)


    class Meta:
        fields = ('email', 'username', 'firstName', 'lastName', 'role', 'password', 'password2')

    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        uid = attrs['uid']
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs
    
    
    def create(self, validated_data):
        uid = validated_data['uid']
        email = validated_data.get('email')
        username = validated_data.get('username')
        firstName = validated_data.get('firstName')
        lastName = validated_data.get('lastName')
        password = validated_data.get('password')

        school_information_instance = get_school_instance(uid)

        user = User.objects.create_user(
                email=email, 
                username= username,
                firstName=firstName,
                lastName=lastName,
                password=password,
                school_id = school_information_instance,
                user_status = UserStatus.Active,
                role=validated_data['role'],
                is_active = True,
                )
        logger.debug(f"Created new user: {user}")
        
        
        return user 
    

class SchoolAdminRegisterSerializer(serializers.Serializer):

    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    email = serializers.EmailField(
            required=False,
            label="Email Optional Contact Information",
            allow_blank=True,
            validators=[UniqueValidator(queryset=User.objects.all())],
            )
    firstName = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="School Admin First Name")
    lastName = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="School Admin Last Name")
    username = serializers.CharField(
        max_length=255, 
        required=True, allow_blank=False, validators=[UniqueValidator(queryset=User.objects.all())],label="User Name or User ID or Email")
    
    role = serializers.ChoiceField(
           label="User Role",
           choices = UserRole.choices
    )

    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=False)
    
    name = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="School Admin Name")
    
    gender = serializers.ChoiceField(
        choices=Gender.choices,
        required=False, allow_blank=True, 
        label="School Admin Gender"
    )
    date_Of_birth = serializers.DateField(required=False, label="School Admin Date of Birth")
    
    phone = PhoneNumberField(required=False,  allow_blank=True, label="School Admin Phone Number or Contact Number")
    joining_date = serializers.DateField(required=False, label="School Admin Name")
    qualification = serializers.CharField(required=False, allow_blank=True,  label="School Admin Qualification")
    experience = serializers.CharField(required=False, allow_blank=True,  label="School Admin Experience")

    

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        uid = attrs['uid']
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        
        uid = validated_data['uid']
        email = validated_data.get('email')
        username = validated_data.get('username')
        firstName = validated_data.get('firstName')
        lastName = validated_data.get('lastName')
        password = validated_data.get('password')
        
        school_information_instance = get_school_instance(uid)

        user_email = email
        
        user = User.objects.create_user(
                username= username,
                firstName=firstName,
                lastName=lastName,
                password=password,
                email=user_email, 
                school_id = school_information_instance,
                user_status = UserStatus.Active,
                role=validated_data['role'],
                is_active = True,
                )
        logger.debug(f"Created new user: {user}")
        
        school_admin_instance = SchoolAdmin.objects.create(
            school_admin_id=school_information_instance,
            schoolUser_id=user.id,
            name=validated_data.get('name'),
            gender=validated_data.get('gender'),
            date_Of_birth=validated_data.get('date_Of_birth'),
            joining_date=validated_data.get('joining_date'),
            qualification=validated_data.get('qualification'),
            experience=validated_data.get('experience'),
            phone=validated_data.get('phone'),
            user_created=self.context['request'].user
        )

        logger.debug(f"Created Student Information: {school_admin_instance}")

        return user
    




class StudentRegisterSerializer(serializers.Serializer):

    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    email = serializers.EmailField(
            required=False,
            label="Email Optional Contact Information",
            allow_blank=True,
            validators=[UniqueValidator(queryset=User.objects.all())],
            )
    firstName = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="Student First Name")
    lastName = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="Student Last Name")
    username = serializers.CharField(
        max_length=255, 
        required=True, allow_blank=False, validators=[UniqueValidator(queryset=User.objects.all())],label="User Name or User ID or Email")
    
    role = serializers.ChoiceField(
           label="User Role",
           choices = UserRole.choices
    )

    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=False)
    
    middle_name = serializers.CharField(max_length=255, required=False, allow_blank=True,  label="Student Middle Name")
    
    gender = serializers.ChoiceField(
        choices=Gender.choices,
        required=False, allow_blank=True, 
        label="Student Gender"
    )
    date_Of_birth = serializers.DateField(required=False, label="Student Date of Birth")
    blood = serializers.ChoiceField(
        choices=BloodGroup.choices,
        required=False, allow_blank=True, 
        label = "Student blood group"
    )
    religion = serializers.ChoiceField(
        choices=Religion.choices,
        required=False, allow_blank=True, 
        label = "Student religion"
    )
    admission_id = serializers.CharField(max_length=255, required=False,  allow_blank=True)
    phone = PhoneNumberField(required=False,  allow_blank=True, label="Student Phone Number or Contact Number")
    student_name_bangla = serializers.CharField(max_length=255, required=False, allow_blank=True, label="Student Full name Bangla")
    student_name_english_captial  = serializers.CharField(max_length=255, required=False,  allow_blank=True, label="Student Full name english capital")
    birth_certificate_number = serializers.CharField(max_length=255, required=False,  allow_blank=True, label="Student Birth Certificate Number")
    birth_of_place = serializers.CharField(max_length=255, required=False,  allow_blank=True, label="Student Birth place Owen district as follow birth_certificate")
    nationality = serializers.CharField(max_length=255, required=False,  allow_blank=True, label="Student Nationality")
    marital_status = serializers.ChoiceField(
        choices=MaritalStatus.choices,
        required=False, allow_blank=True, 
        label = "Student marital status"
    )
    disability_status = serializers.ChoiceField(
        choices=DisabilityStatus.choices,
        required=False, allow_blank=True, 
        label = "Student Disability Status"
    )
    ethnic_status = serializers.ChoiceField(
        choices=EthnicGroup.choices,
        required=False, allow_blank=True, 
        label = "Student Ethnic Status"
    )

    class Meta:
        fields =(
            'email', 
            'username', 
            'firstName', 
            'lastName', 
            'role', 
            'password', 
            'password2',
            'middle_name', 
            'gender', 
            'date_Of_birth', 
            'blood', 
            'religion', 
            'admission_id', 
            'phone', 
            'student_name_bangla', 
            'student_name_english_captial', 
            'birth_certificate_number', 
            'birth_of_place', 
            'nationality', 
            'marital_status', 
            'disability_status', 
            'ethnic_status')
    

    

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        uid = attrs['uid']
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        
        uid = validated_data['uid']
        email = validated_data.get('email')
        username = validated_data.get('username')
        firstName = validated_data.get('firstName')
        lastName = validated_data.get('lastName')
        password = validated_data.get('password')
        
        school_information_instance = get_school_instance(uid)

        user_email = email
        
        user = User.objects.create_user(
                username= username,
                firstName=firstName,
                lastName=lastName,
                password=password,
                email=user_email, 
                school_id = school_information_instance,
                user_status = UserStatus.Active,
                role=validated_data['role'],
                is_active = True,
                )
        logger.debug(f"Created new user: {user}")
        
        student_instance = Student.objects.create(
            school_student_id=school_information_instance,
            student_user_id=user.id,
            middle_name=validated_data.get('middle_name'),
            gender=validated_data.get('gender'),
            date_Of_birth=validated_data.get('date_Of_birth'),
            blood=validated_data.get('blood'),
            religion=validated_data.get('religion'),
            admission_id=validated_data.get('admission_id'),
            phone=validated_data.get('phone'),
            student_name_bangla=validated_data.get('student_name_bangla'),
            student_name_english_captial=validated_data.get('student_name_english_captial'),
            birth_certificate_number=validated_data.get('birth_certificate_number'),
            birth_of_place=validated_data.get('birth_of_place'),
            nationality=validated_data.get('nationality'),
            marital_status=validated_data.get('marital_status'),
            disability_status=validated_data.get('disability_status'),
            ethnic_status=validated_data.get('ethnic_status'),
            user_created=self.context['request'].user
        )

        logger.debug(f"Created Student Information: {student_instance}")

        return user