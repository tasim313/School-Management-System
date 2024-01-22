"""Serializers for Transport Model"""

from rest_framework import serializers

from SchoolAdminApp.models import Transport

from common.models import SchoolInformationOnBoarding


class TransportListSerializer(serializers.ModelSerializer):
    school_transport = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Transport
        fields = [
            "uid",
            "slug",
            "school_transport",
            "route_name",
            "vehicle_number",
            "driver_name",
            "license_number",
            "contact_number",
            "driver_address",
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
