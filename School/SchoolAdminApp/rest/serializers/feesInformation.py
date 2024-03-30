from rest_framework import serializers

from SchoolAdminApp.models import FeesInformation, FeesCategory
from core.models import SchoolClass, SchoolSection


class FeesCategorySlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesCategory
        fields = [
            "uid",
            "name",
        ]


class SchoolClassSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = [
            "uid",
            "slug",
            "name",
            "total_students",
            "present_students",
            "absent_students",
        ]


class SchoolSectionSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSection
        fields = [
            "uid",
            "slug",
            "name"
        ]


class FeesInformationSerializer(serializers.ModelSerializer):
    fees_category = serializers.SlugRelatedField(
        queryset=FeesCategory.objects.all(),
        slug_field="uid",
    )
    fess_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )
    fess_section = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = FeesInformation
        fields = [
            "uid",
            "fees_amount",
            "fees_start",
            "fees_end",
            'fees_category',
            'fess_class',
            'fess_section'
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


class FeesInformationDetailSerializer(serializers.ModelSerializer):
    fees_category = FeesCategorySlimSerializer()
    fess_class = SchoolClassSlimSerializer()
    fess_section = SchoolSectionSlimSerializer()

    class Meta:
        model = FeesInformation
        fields = [
            "uid",
            "fees_amount",
            "fees_start",
            "fees_end",
            'fees_category',
            'fess_class',
            'fess_section'
        ]
        read_only_fields = [
            "uid",
            "fees_amount",
            "fees_start",
            "fees_end",
            "fees_category",
            "fess_class",
            "fess_section"
        ]
