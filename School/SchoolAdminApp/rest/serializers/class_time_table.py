"""Serializer for ClassTimeTable model."""

from rest_framework import serializers

from SchoolAdminApp.models import ClassTimeTable, Subject
from common.models import SchoolInformationOnBoarding
from core.models import SchoolClass, SchoolSection

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

class SchoolSectionSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSection
        fields = [
            "uid",
            "slug",
            "name",
            'school_class'
        ]

class SchoolSubjectSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            "uid",
            "subject_id",
            "name",
            "school_subject",
            "class_subject"
        ]

class ClassTimeTableListSerializer(serializers.ModelSerializer):
    """Serializer for ClassTimeTable model."""

    school_class_time_table = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    school_time_table = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )
    school_section_time_table = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(),
        slug_field="uid",
    )
    class_time_table_subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = ClassTimeTable
        fields = [
            "uid",
            "slug",
            "school_class_time_table",
            "school_time_table",
            "school_section_time_table",
            "class_time_table_subject",
            "teacher_id",
            "name",
            "class_date",
            "class_start_time",
            "class_end_time",
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        """Create method for ClassTimeTable model"""
        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        """Update method for ClassTimeTable model"""
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance


class ClassTimeTableDetailsSerializer(serializers.ModelSerializer):
    school_class_time_table = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    school_time_table = SchoolClassSlimSerializer()
    school_section_time_table = SchoolSectionSlimSerializer()
    class_time_table_subject = SchoolSubjectSlimSerializer()

    class Meta:
        model = ClassTimeTable
        fields = [
            "uid",
            "slug",
            "school_class_time_table",
            "school_time_table",
            "school_section_time_table",
            "class_time_table_subject",
            "teacher_id",
            "name",
            "class_date",
            "class_start_time",
            "class_end_time",
        ]
        read_only_fields = ["uid", "slug"]