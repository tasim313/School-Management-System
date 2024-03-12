"""Serializers for Library Model"""

from rest_framework import serializers

from SchoolAdminApp.models import Library, Department

from common.models import SchoolInformationOnBoarding

from core.models import SchoolClass


class SchoolClassSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = [
            "uid",
            "slug",
            "name",
            "total_students",
            "present_students",
            "absent_students",
        ]


class SchoolDepartmentSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "uid",
            "department_id",
            "name",
            "head_of_department",
        ]


class LibraryListSerializer(serializers.ModelSerializer):
    school_library = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    library_department = serializers.SlugRelatedField(
        queryset=Department.objects.all(),
        slug_field="uid",
    )
    library_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
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


class LibraryDetailSerializer(serializers.ModelSerializer):
    school_library = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    library_department = SchoolDepartmentSlimSerializer(read_only=True)
    library_class = SchoolClassSlimSerializer(read_only=True)

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
