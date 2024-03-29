from rest_framework import serializers

from SchoolAdminApp.models import  FeesCategory, FeesCollection
from common.models import SchoolInformationOnBoarding
from StudentApp.models import Student


class SchoolFeesCategorySlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesCategory
        fields = [
            "uid",
            "name"
        ]


class FeesCollectionSerializer(serializers.ModelSerializer):
    
    fees_collection_category = serializers.SlugRelatedField(
        queryset=FeesCategory.objects.all(),
        slug_field="uid",
    )
    school_fees_collection = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    student_fees_collection = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = FeesCollection
        fields = [
            "uid",
            "fees_amount",
            "paid_date",
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

