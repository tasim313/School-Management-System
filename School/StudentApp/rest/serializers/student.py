from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.serializerfields import PhoneNumberField

from ...models import (
    Student,
    StudentImage,
    StudentCurrentStatus,
    StudentPermanentAddress,
    StudentPresentAddress,
    StudentFather,
    StudentMother,
    StudentGuardian
)

from school_auth.models import (
    User
)

from core.models import (
    SchoolClass,
    SchoolSection
)

from school_auth.choice import (
    UserRole, UserStatus
)

from StudentApp.choice import (
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


class StudentImageSerializer(serializers.ModelSerializer):
    student_info = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentImage
        fields = [
            "uid",
            "slug",
            "image",
            "student_info"
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentCurrentStatusSerializer(serializers.ModelSerializer):
    student_current_status = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )
    current_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )
    current_section = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentCurrentStatus
        fields = [
            "uid",
            "slug",
            "class_roll_number",
            "student_current_status",
            "current_class",
            "current_section"
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentPermanentAddressSerializer(serializers.ModelSerializer):
    student_permanent_address = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentPermanentAddress
        fields = [
            "uid",
            "slug",
            "divisions",
            "district",
            "upazila",
            "pourashava",
            'union_parishad',
            'ward',
            'mouza',
            'village',
            'house_holding_number',
            'post_office',
            'post_code',
            'student_permanent_address'
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentPresentAddressSerializer(serializers.ModelSerializer):
    student_present_address = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentPresentAddress
        fields = [
            "uid",
            "slug",
            "divisions",
            "district",
            "upazila",
            "pourashava",
            'union_parishad',
            'ward',
            'mouza',
            'village',
            'house_holding_number',
            'post_office',
            'post_code',
            'student_present_address'
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentFatherSerializer(serializers.ModelSerializer):
    student_father = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentFather
        fields = [
            "uid",
            "name_bangla",
            "name_english_capital",
            "nid",
            "date_of_birth",
            'birth_certificate_number',
            'phone',
            'occupation',
            'father_status',
            'date_of_death',
            'student_father'
        ]
        read_only_fields = ["uid", ]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentMotherSerializer(serializers.ModelSerializer):
    student_mother = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentMother
        fields = [
            "uid",
            "name_bangla",
            "name_english_capital",
            "nid",
            "date_of_birth",
            'birth_certificate_number',
            'phone',
            'occupation',
            'mother_status',
            'date_of_death',
            'student_mother'
        ]
        read_only_fields = ["uid", ]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentGuardianSerializer(serializers.ModelSerializer):
    student_guardian = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = StudentGuardian
        fields = [
            "uid",
            "name",
            "nid",
            "occupation",
            'guardian_status',
            'phone',
            'student_guardian'
        ]
        read_only_fields = ["uid", ]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class StudentDetailInformationListSerializer(serializers.ModelSerializer):
    student_father_name_capital = serializers.CharField(source='father_name', read_only=True)
    student_mother_name_capital = serializers.CharField(source='mother_name', read_only=True)
    student_village_name = serializers.CharField(source='village_name', read_only=True)
    student_post_office_name = serializers.CharField(source='post_office_name', read_only=True)
    student_upazila_name = serializers.CharField(source='upazila_name', read_only=True)
    student_district_name = serializers.CharField(source='district_name', read_only=True)

    class Meta:
        model = Student
        fields = [
            "uid",
            "slug",
            "student_name_english_captial",
            "student_name_bangla",
            "phone",
            "nationality",
            "student_father_name_capital",
            "student_mother_name_capital",
            "student_village_name",
            "student_post_office_name",
            "student_upazila_name",
            "student_district_name",
        ]
        read_only_fields = ["uid", "slug", "phone", "student_name_bangla", "nationality",]
