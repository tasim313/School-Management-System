from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from common.choice import SchoolType

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


class AcademicInformationListSerializer(serializers.ModelSerializer):
    school_academic_information = SchoolWebsiteLiteSerializer(read_only=True)
    website_info_uid = serializers.UUIDField(write_only=True, required=False)
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
            # "title",
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
            "school_name",
            "school_address",
            "school_phone",
            "school_type",
            "website_name",
        ]

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user

        website_name = validated_data.pop("website_name", None)
        website_logo = validated_data.pop("website_logo", None)
        website_favicon = validated_data.pop("website_favicon", None)
        address = validated_data.pop("address", None)
        website_info_uuid = validated_data.pop("website_info_uuid", None)
        # onboard school data
        school_name = validated_data.pop("school_name", None)
        school_address = validated_data.pop("school_address", None)
        school_phone = validated_data.pop("school_phone", None)
        school_type = validated_data.pop("school_type", None)
        # Retrieve the school if it exists, or create it if it doesn't
        school, created = SchoolInformationOnBoarding.objects.get_or_create(
            name=school_name,
            address=school_address,
            defaults={
                "phone": school_phone,
                "school_type": school_type,
            },
        )
        website_info = None
        # if website info is provided then we retrieve and use it
        if website_info_uuid:
            website_info = WebsiteInformation.objects.filter(uid=website_info_uuid)

            # website uid is not given or not by the uuid but info is given then
            # we create it with given info
            if not website_info.exists():
                website_info = WebsiteInformation.objects.create(
                    school_website_id=school.id,
                    name=website_name,
                    logo=website_logo,
                    favicon=website_favicon,
                    user_created=user,
                    status=Status.Active,
                )
                validated_data["school_admission"] = website_info
            else:
                validated_data["school_admission"] = website_info
        else:
            website_info = WebsiteInformation.objects.create(
                school_website_id=school.id,
                name=website_name,
                logo=website_logo,
                favicon=website_favicon,
                user_created=user,
                status=Status.Active,
            )
            validated_data["school_admission"] = website_info
        return super().create(validated_data)
