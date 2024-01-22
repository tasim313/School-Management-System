"""Serializers for Library Model"""

from rest_framework import serializers

from SchoolAdminApp.models import Library

from common.models import SchoolInformationOnBoarding


class LibraryListSerializer(serializers.ModelSerializer):
    school_library = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Library
        fields = [
            "uid",
            "slug",
            "school_library",
            "library_department",
            "library_class",
            "book_id",
            "book_name",
            "language",
            "book_type",
            "book_status",
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
