from rest_framework import serializers

from SchoolAdminApp.models import Subject

from common.models import SchoolInformationOnBoarding
from core.models import SchoolClass


class SchoolClassSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = [
            "uid",
            "slug",
            "name"
        ]



class SubjectListSerializer(serializers.ModelSerializer):
    school_subject = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    class_subject = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = Subject
        fields = [
            "uid",
            "subject_id",
            "name",
            "school_subject",
            "class_subject"
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



class SubjectDetailSerializer(serializers.ModelSerializer):
    school_subject = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    class_subject = SchoolClassSlimSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = [
            "uid",
            "subject_id",
            "name",
            "school_subject",
            "class_subject"
        ]
        read_only_fields = ["uid"]