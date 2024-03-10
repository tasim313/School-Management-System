from rest_framework import serializers

from SchoolAdminApp.models import EmployeeCandidate, Career
from common.models import SchoolInformationOnBoarding


class EmployeeCandidateSerializer(serializers.ModelSerializer):
    school_candidate = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    job_category = serializers.SlugRelatedField(
        queryset=Career.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = EmployeeCandidate
        fields = [
            "uid",
            "slug",
            "name",
            "email",
            "phone_number",
            "portfolio_link",
            "linkedin_link",
            "comment",
            "curriculum_vitae",
            'school_candidate',
            'job_category'
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
