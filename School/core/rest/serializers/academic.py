from dataclasses import fields
from requests import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from phonenumber_field.serializerfields import PhoneNumberField

from common.choice import SchoolType
from common.mixins import WebsiteInfoMixin, SchoolInfoMixin
from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)
from core.models import (
    AcademicInformation,
    SchoolInformationOnBoarding,
    WebsiteInformation,
)

from ...utills import (
    get_school_website_logo,
    get_school_website_favicon,
)

from core.choice import Status
from core.rest.serializers.websiteInfo import SchoolWebsiteLiteSerializer

# from core.utills import get_or_create_website_info


class AcademicInformationListSerializer(
    WebsiteInfoMixin,
    SchoolInfoMixin,
    ModelSerializer,
):
    school_academic_information = SchoolWebsiteLiteSerializer(read_only=True)
    website_info_uid = serializers.UUIDField(write_only=True, required=False)
    school_uid = serializers.UUIDField(write_only=True, required=False)
    website_name = serializers.CharField(
        max_length=2000,
        allow_blank=True,
        write_only=True,
        required=False,
    )
    website_logo = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=get_school_website_logo,
        label="School Logo",
        required=False,
        write_only=True,
    )
    website_favicon = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=get_school_website_favicon,
        label="Favicon Icon",
        required=False,
        write_only=True,
    )
    # school information optional
    school_name = serializers.CharField(
        max_length=2000,
        allow_blank=True,
        write_only=True,
        required=False,
    )
    school_address = serializers.CharField(
        max_length=2000,
        allow_blank=True,
        write_only=True,
        required=False,
    )
    school_phone = PhoneNumberField(
        required=False,
        allow_blank=True,
        write_only=True,
    )
    school_type = serializers.ChoiceField(
        SchoolType.choices,
        required=False,
        allow_blank=True,
        write_only=True,
    )

    class Meta:
        model = AcademicInformation
        fields = [
            "id",
            "uid",
            "slug",
            "title",
            "code_of_conducts",
            "guideline_for_parents",
            "dress_code",
            "homework_and_lecture_documents",
            "lesson_plan",
            "academic_calendar",
            "syllabus",
            "class_routine",
            "co_curricular_activities",
            "school_academic_information",
            # website information
            "website_name",
            "website_logo",
            "website_favicon",
            "website_info_uid",
            # school information
            "school_uid",
            "school_name",
            "school_address",
            "school_phone",
            "school_type",
            "website_name",
        ]

    def create(self, validated_data):
        school = self.create_or_get_school_info(validated_data)
        validated_data = self.create_or_get_website_info(validated_data, school)
        return super().create(validated_data)


class AcademicInformationDetailSerializer(ModelSerializer):
    school_academic_information = SchoolWebsiteLiteSerializer(read_only=True)
    school_information = SchoolInformationOnBoardingListSerializer(
        source="school_academic_information__school_website",
        read_only=True,
    )
    website_info_uid = serializers.UUIDField(write_only=True, required=False)
    # school_uid = serializers.UUIDField(write_only=True, required=False)

    class Meta:
        model = AcademicInformation
        fields = [
            "id",
            "uid",
            "slug",
            "title",
            "code_of_conducts",
            "guideline_for_parents",
            "dress_code",
            "homework_and_lecture_documents",
            "lesson_plan",
            "academic_calendar",
            "syllabus",
            "class_routine",
            "co_curricular_activities",
            "school_academic_information",
            "school_information",
            # uid related fields
            "website_info_uid",
            # "school_uid",
        ]

    def update(self, instance, validated_data):
        # school_uid = validated_data.pop("school_uid", None)
        website_info_uid = validated_data.pop("website_info_uid", None)
        if website_info_uid:
            try:
                school_academic_information = WebsiteInformation().objects.get(
                    uid=website_info_uid
                )
                validated_data[
                    "school_academic_information"
                ] = school_academic_information
            except WebsiteInformation.DoesNotExist:
                return serializers.ValidationError(
                    {"detail": "Given WebsiteInformation Doesn't Exists!"}
                )
        return super().update(instance, validated_data)
