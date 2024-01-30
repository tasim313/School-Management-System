from rest_framework import serializers

from core.models import AlumniSection, AlumniSectionImage
from common.models import SchoolInformationOnBoarding



class AlumniSectionListSerializer(serializers.ModelSerializer):
    
    school_alumni_section = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = AlumniSection
        fields = [
            "uid",
            "slug",
            "about_alumni",
            "alumni_events",
            "alumni_news",
            'school_alumni_section',
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



class AlumniSectionImageListSerializer(serializers.ModelSerializer):
    
    alumni_info = serializers.SlugRelatedField(
        queryset=AlumniSection.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = AlumniSectionImage
        fields = [
            "uid",
            "slug",
            "image",
            'alumni_info',
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
