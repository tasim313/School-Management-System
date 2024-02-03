"""Serializers for GradingConfig model."""

from rest_framework import serializers

from SchoolAdminApp.models import GradingConfig
from common.models import SchoolInformationOnBoarding


class GradingConfigListSerializer(serializers.ModelSerializer):
    school_grading = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = GradingConfig
        fields = [
            "uid",
            "slug",
            "school_grading",
            "letter_grade_A_plus",
            "letter_grade_A",
            "letter_grade_A_minus",
            "letter_grade_B",
            "letter_grade_C",
            "letter_grade_D",
            "letter_grade_F",
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        """Create method for GradingConfig."""
        school_grading = validated_data.get('school_grading')

        # Check if a GradingConfig already exists for the specified school_grading
        if GradingConfig.objects.filter(school_grading_id=school_grading.id).exists():
            raise serializers.ValidationError(
                {"detail": "GradingConfig already exists for this school."}
            )

        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        """Update method for GradingConfig."""
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
