from rest_framework import serializers

from SchoolAdminApp.models import Career, Department
from common.models import SchoolInformationOnBoarding


class CareerListSerializer(serializers.ModelSerializer):
    school_career = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    career_department = serializers.SlugRelatedField(
        queryset=Department.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Career
        fields = [
            "uid",
            "slug",
            "title",
            "location",
            "experience",
            "no_of_vacancies",
            "age_limit",
            "salary_from",
            "salary_to",
            "job_type",
            "job_status",
            'start_date',
            'expired_date',
            'description',
            'school_career',
            'career_department'
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
