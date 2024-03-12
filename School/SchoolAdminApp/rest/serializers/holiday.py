from rest_framework import serializers

from SchoolAdminApp.models import HolidayManagement

from common.models import SchoolInformationOnBoarding


class HolidayManagementListSerializer(serializers.ModelSerializer):
    school_holiday = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = HolidayManagement
        fields = [
            "uid",
            "slug",
            "school_holiday",
            "name",
            "holiday_type",
            "holiday_start",
            "holiday_end",

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
