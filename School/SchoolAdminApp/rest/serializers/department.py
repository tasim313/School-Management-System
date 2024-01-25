from rest_framework import serializers

from SchoolAdminApp.models import Department

from common.models import SchoolInformationOnBoarding


class DepartmentListSerializer(serializers.ModelSerializer):
    school_department = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Department
        fields = [
            "uid",
            "department_id",
            "name",
            "head_of_department",
            "school_department"
        ]
        read_only_fields = ["uid"]

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
