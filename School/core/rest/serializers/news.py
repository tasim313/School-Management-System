from dataclasses import fields
from tkinter import NO
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.rest.serializers.websiteInfo import SchoolWebsiteLiteSerializer
from core.models import NewsEvents, WebsiteInformation

from common.mixins import WebsiteInfoMixin

from ...utills import (
    get_school_website_logo,
    get_school_website_favicon,
)


class NewsEventListSerializer(WebsiteInfoMixin, ModelSerializer):
    school_website_news_events = SchoolWebsiteLiteSerializer(read_only=True)
    website_info_uid = serializers.UUIDField(write_only=True, required=False)

    # website info fields
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

    class Meta:
        model = NewsEvents
        fields = [
            "id",
            "uid",
            "slug",
            "school_website_news_events",
            "news_events_status",
            "headline",
            "description",
            "publish_date",
            "image",
            "website_name",
            "website_logo",
            "website_favicon",
            "website_info_uid",
        ]

    def create(self, validated_data):
        website_info_uid = validated_data.pop("website_info_uid", None)

        if website_info_uid:
            validated_data[
                "school_website_news_events"
            ] = WebsiteInformation.objects.get(uid=website_info_uid)
        return super().create(validated_data)
