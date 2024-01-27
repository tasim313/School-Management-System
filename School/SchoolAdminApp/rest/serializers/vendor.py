from rest_framework import serializers

from SchoolAdminApp.models import Vendor

from common.models import SchoolInformationOnBoarding


class VendorListSerializer(serializers.ModelSerializer):
    school_vendor = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    
    class Meta:
        model = Vendor
        fields = [
            "uid",
            "slug",
            "name",
            "address",
            "phone_number",
            "school_vendor"
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
