from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from core.models import SchoolAdmission, WebsiteInformation, SchoolInformationOnBoarding
from core.choice import Status
from core.rest.serializers.websiteInfo import SchoolWebsiteLiteSerializer

from common.choice import SchoolType


from ...utills import (
    get_school_website_logo,
    get_school_website_favicon,
)


class SchoolAdmissionSerializer(ModelSerializer):
    school_admission = SchoolWebsiteLiteSerializer(
        read_only=True
    )
    name = serializers.CharField(
        max_length=255,
        trim_whitespace=True,
        write_only=True,
        required=False
    )
    address = serializers.CharField(
        max_length = 2000,
        allow_blank=True,
        write_only=True,
        required=False
    )
    phone = PhoneNumberField(
        required=False,
        allow_blank=True,
        write_only=True,
    )
    school_type = serializers.ChoiceField(
        choices=SchoolType.choices,
        required=False
    )
    school_name = serializers.CharField(
        max_length = 2000,
        allow_blank=True,
        write_only=True,
        required=False
    )
    school_address = serializers.CharField(
        max_length = 2000,
        allow_blank=True,
        write_only=True,
        required=False
    )
    school_phone = PhoneNumberField(
        required=False,
        allow_blank=True,
        write_only=True
    )
    logo = serializers.ImageField(max_length=None,
        allow_empty_file=False,
        use_url=get_school_website_logo,
        label="School Logo",
        required=False,
        write_only=True
    )
    favicon = serializers.ImageField(max_length=None,
        allow_empty_file=False,
        use_url=get_school_website_favicon,
        label="Favicon Icon",
        required=False,
        write_only=True
    )
    website_info_uuid = serializers.UUIDField(
        write_only=True,
        required=False,
    )

    class Meta:
        model = SchoolAdmission
        fields = [
            "id",
            "uid",
            "title",
            "admission_class",
            "admission_branch",
            "admission_division",
            "number_of_seats",
            "limit_of_age",
            "collection_of_prospectus",
            "fill_the_application_form",
            "online_admission_form_date_time",
            "admission_process_college_information_website",
            "digital_lottery_time_information",
            "admission_application_rules",
            "other_description",
            "remark",
            "pdf_file",
            "name",
            "address",
            "phone",
            "school_name",
            "school_address",
            "school_phone",
            "school_type",
            "school_admission",
            "logo",
            "favicon",
            "website_info_uuid"
        ]

    def create(self, validated_data):
        request = self.context['request']
        user = request.user

        name = validated_data.pop("name", None)
        logo = validated_data.pop("logo", None)
        favicon = validated_data.pop("favicon", None)
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
                'phone': school_phone,
                'school_type': school_type,
            }
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
                    name=name,
                    logo=logo,
                    favicon=favicon,
                    user_created=user,
                    status=Status.Active,
                )
                validated_data["school_admission"] = website_info
            else:
                validated_data["school_admission"] = website_info
        else:
            website_info = WebsiteInformation.objects.create(
                    school_website_id=school.id,
                    name=name,
                    logo=logo,
                    favicon=favicon,
                    user_created=user,
                    status=Status.Active,
                )
            validated_data["school_admission"] = website_info

        admission = SchoolAdmission.objects.create(
            **validated_data
        )

        return admission


class SchoolAdmissionEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolAdmission
        fields = [
            "id",
            "uid",
            "title",
            "admission_class",
            "admission_branch",
            "admission_division",
            "number_of_seats",
            "limit_of_age",
            "collection_of_prospectus",
            "fill_the_application_form",
            "online_admission_form_date_time",
            "admission_process_college_information_website",
            "digital_lottery_time_information",
            "admission_application_rules",
            "other_description",
            "remark",
            "pdf_file",
        ]