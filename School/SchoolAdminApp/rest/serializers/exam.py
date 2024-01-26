"""Serializers for Exam models."""

from rest_framework import serializers

from SchoolAdminApp.models import Exam, Subject
from common.models import SchoolInformationOnBoarding
from core.models import SchoolClass, SchoolSection


class ExamListSerializer(serializers.ModelSerializer):

    school_exam = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    exam_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )
    exam_section = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(),
        slug_field="uid",
    )
    exam_subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Exam
        fields = [
            "uid",
            "slug",
            "school_exam",
            "exam_class",
            "exam_section",
            "exam_subject",
            "name",
            "fees",
            "exam_start_time",
            "exam_end_time",
            "exam_date",
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        """Create method for Exam model"""
        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        """Update method for Exam model"""
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
