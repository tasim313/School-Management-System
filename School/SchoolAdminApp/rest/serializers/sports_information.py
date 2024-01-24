"""Serializer for SportsInformation Model"""

from rest_framework import serializers

from SchoolAdminApp.models import SportsInformation
from common.models import SchoolInformationOnBoarding


class SportsInformationListSerializer(serializers.ModelSerializer):
    school_sports = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
        error_messages={"school_sports": "School does not exist"},
    )

    class Meta:
        model = SportsInformation
        fields = [
            "uid",
            "slug",
            "school_sports",
            "sports_id",
            "sports_name",
            "coach_name",
            "started_year",
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
