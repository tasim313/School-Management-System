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
