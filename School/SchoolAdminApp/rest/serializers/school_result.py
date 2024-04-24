"""Serializers for SchoolResult model"""

from rest_framework import serializers

from SchoolAdminApp.models import (
    SchoolResult,
    Semester,
    Student,
    SchoolInformationOnBoarding,
    Result,
)
from core.models import SchoolClass, SchoolSection


class SchoolSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInformationOnBoarding
        fields = [
            "uid",
            "name",
            "phone"
        ]


class SchoolClassSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = [
            "uid",
            "name"
        ]


class SchoolSectionSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSection
        fields = [
            "uid",
            "name"
        ]


class SchoolSemesterSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = [
            "uid",
            "name"
        ]


class ResultSlimSerializer(serializers.ModelSerializer):
    result_subject_uid = serializers.CharField(source="result_subject.uid")
    result_subject_name = serializers.CharField(source="result_subject.name")

    class Meta:
        model = Result
        fields = [
            "uid",
            "result_subject_uid",
            "result_subject_name",
            "mark",
            "gpa",
            "grade",
        ]


class StudentSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "uid",
            "student_name_english_captial",
            "student_name_bangla",
        ]


class SchoolResultListSerializer(serializers.ModelSerializer):
    school = SchoolSlimSerializer()
    school_class = SchoolClassSlimSerializer()
    school_section = SchoolSectionSlimSerializer()
    school_semester = SchoolSemesterSlimSerializer()
    school_student = StudentSlimSerializer()
    passed_subjects_result = ResultSlimSerializer(many=True)
    failed_subjects_result = ResultSlimSerializer(many=True)

    class Meta:
        model = SchoolResult
        fields = [
            "uid",
            "school",
            "school_class",
            "school_section",
            "school_semester",
            "school_student",
            "total_marks",
            "cgpa",
            "grade",
            "passed_subjects_result",
            "failed_subjects_result",
            "createdAt",
            "updateAt",
        ]
        read_only_fields = ("uid",)
