"""Serializers for Testimonial model"""

from django.utils import timezone

from rest_framework import serializers
from SchoolAdminApp.models import Testimonial
from StudentApp.models import Student
from common.models import SchoolInformationOnBoarding


class TestimonialSerializer(serializers.ModelSerializer):
    school_testimonial = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    student_testimonial = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Testimonial
        fields = [
            "uid",
            "school_testimonial",
            "student_testimonial",
            "student_passing_year",
            "student_gpa",
            "student_session",
            "student_roll",
            "student_reg",
            "student_board",
            "student_exam_center",
            "testimonial_serial_number",
            "testimonial_issue_date",
        ]
        read_only_fields = ('uid', "testimonial_serial_number", "testimonial_issue_date")

    def create(self, validated_data):
        student = validated_data.get("student_testimonial")

        # Check if the student is already have a testimonial
        if Testimonial.objects.filter(student_testimonial__id=student.id).exists():
            raise serializers.ValidationError(
                {"student_testimonial": "Student already have a testimonial"}
            )

        # Create testimonial
        instance = super().create(validated_data=validated_data)

        # Set testimonial_issue_date to current date
        instance.testimonial_issue_date = timezone.now().date()

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created", "testimonial_issue_date"])

        return instance

    def update(self, instance, validated_data):
        # Update testimonial
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
