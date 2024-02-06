"""Serializer for Result model."""

from rest_framework import serializers

from SchoolAdminApp.models import (
    Result,
    SchoolClass,
    SchoolSection,
    Semester,
    Subject,
    Student
)
from SchoolAdminApp.helper import get_gpa_and_grade
from common.models import SchoolInformationOnBoarding


class ResultListSerializer(serializers.ModelSerializer):
    school_result = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    result_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )
    result_section = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(),
        slug_field="uid",
    )
    result_semester = serializers.SlugRelatedField(
        queryset=Semester.objects.all(),
        slug_field="uid",
    )
    result_subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field="uid",
    )
    result_student = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Result
        fields = [
            "uid",
            "school_result",
            "result_class",
            "result_section",
            "result_semester",
            "result_subject",
            "result_student",
            "mark",
            "gpa",
            "grade",
        ]
        read_only_fields = ["uid", "gpa", "grade"]

    def create(self, validated_data):
        # Get gpa and grade
        mark = validated_data.get("mark", None)
        school = validated_data.get("school_result", None)
        gpa, grade = get_gpa_and_grade(mark, school.id)

        # Add gpa and grade to validated_data
        validated_data["gpa"] = gpa
        validated_data["grade"] = grade

        # Create instance
        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        # Get gpa and grade
        mark = validated_data.get("mark", None)
        school = validated_data.get("school_result", None)
        gpa, grade = get_gpa_and_grade(mark, school.id)

        # Add gpa and grade to validated_data
        validated_data["gpa"] = gpa
        validated_data["grade"] = grade

        # Update instance
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
