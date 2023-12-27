from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.rest.serializers.websiteInfo import SchoolWebsiteLiteSerializer
from core.models import NewsEvents, WebsiteInformation

from common.mixins import WebsiteInfoMixin
from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)


class NewsEventListSerializer(WebsiteInfoMixin, ModelSerializer):
    school_website_news_events = SchoolWebsiteLiteSerializer(read_only=True)
    website_info_uid = serializers.UUIDField(write_only=True, required=False)
    school = SchoolInformationOnBoardingListSerializer(read_only=True)

    class Meta:
        model = NewsEvents
        fields = [
            "id",
            "uid",
            "slug",
            "school_website_news_events",
            "school",
            "news_events_status",
            "headline",
            "description",
            "publish_date",
            "image",
            "website_info_uid",
        ]

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def create(self, validated_data):
        request = self.context["request"]
        website_info_uid = validated_data.pop("website_info_uid", None)

        if website_info_uid:
            try:
                website = WebsiteInformation.objects.get(uid=website_info_uid)
                validated_data["school_website_news_events"] = website
            except WebsiteInformation.DoesNotExist:
                serializers.ValidationError("Website info not found!")

        validated_data["school"] = request.user.school
        return super().create(validated_data)
