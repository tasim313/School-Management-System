"""Serializer for Result model."""

from django.db import transaction

from rest_framework import serializers

from SchoolAdminApp.helper import get_gpa_and_grade, calculate_student_cgpa
from SchoolAdminApp.models import (
    Result,
    SchoolClass,
    SchoolSection,
    Semester,
    Subject,
    Student
)

from common.models import SchoolInformationOnBoarding


class ResultListSerializer(serializers.ModelSerializer):
    school_result = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
        required=True
    )
    result_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
        required=True
    )
    result_section = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(),
        slug_field="uid",
        required=True
    )
    result_semester = serializers.SlugRelatedField(
        queryset=Semester.objects.all(),
        slug_field="uid",
        required=True
    )
    result_subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field="uid",
        required=True
    )
    result_student = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
        required=True
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

    @transaction.atomic
    def create(self, validated_data):
        school_result = validated_data.get("school_result", None)
        result_class = validated_data.get("result_class", None)
        result_section = validated_data.get("result_section", None)
        result_semester = validated_data.get("result_semester", None)
        result_subject = validated_data.get("result_subject", None)
        result_student = validated_data.get("result_student", None)

        # Check if result already exists
        result = Result.objects.filter(
            school_result=school_result,
            result_class=result_class,
            result_section=result_section,
            result_semester=result_semester,
            result_subject=result_subject,
            result_student=result_student,
        ).exists()

        if result:
            raise serializers.ValidationError(
                {"detail": "Result already exists."}
            )

        user = self.context["request"].user
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
        instance.user_created = user
        instance.save(update_fields=["user_created"])

        # Calculate student cgpa
        school_result_instance = calculate_student_cgpa(instance)
        # Add user_created by request user
        school_result_instance.user_created = user
        school_result_instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        user = self.context["request"].user
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
        instance.user_updated = user
        instance.save(update_fields=["user_updated"])

        # Calculate student cgpa
        school_result_instance = calculate_student_cgpa(instance)
        # Add user_updated by request user
        school_result_instance.user_updated = user
        school_result_instance.save(update_fields=["user_updated"])

        return instance
