from core.models import WebsiteInformation, SchoolInformationOnBoarding
from core.choice import Status


class WebsiteInfoMixin:
    def create_or_get_website_info(self, validated_data, school):
        website_name = validated_data.pop("website_name", None)
        website_logo = validated_data.pop("website_logo", None)
        website_favicon = validated_data.pop("website_favicon", None)
        website_info_uuid = validated_data.pop("website_info_uid", None)

        website_info = None

        if website_info_uuid:
            website_info = WebsiteInformation.objects.filter(uid=website_info_uuid)

            if not website_info.exists():
                website_info = WebsiteInformation.objects.create(
                    school_website_id=school.id,
                    name=website_name,
                    logo=website_logo,
                    favicon=website_favicon,
                    user_created=self.context["request"].user,
                    status=Status.Active,
                )
                validated_data["school_academic_information"] = website_info
            else:
                validated_data["school_academic_information"] = website_info.first()
        else:
            website_info = WebsiteInformation.objects.create(
                school_website_id=school.id,
                name=website_name,
                logo=website_logo,
                favicon=website_favicon,
                user_created=self.context["request"].user,
                status=Status.Active,
            )
            validated_data["school_academic_information"] = website_info

        return validated_data


class SchoolInfoMixin:
    def create_or_get_school_info(self, validated_data):
        school_name = validated_data.pop("school_name", None)
        school_address = validated_data.pop("school_address", None)
        school_phone = validated_data.pop("school_phone", None)
        school_type = validated_data.pop("school_type", None)
        school_uid = validated_data.pop("school_uid", None)
        if school_uid:
            school = SchoolInformationOnBoarding.objects.get(uid=school_uid)
        else:
            school = SchoolInformationOnBoarding.objects.create(
                name=school_name,
                phone=school_phone,
                address=school_address,
                school_type=school_type,
            )

        return school
