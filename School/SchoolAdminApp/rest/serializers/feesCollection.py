from rest_framework import serializers

from SchoolAdminApp.models import  FeesCategory, FeesCollection
from common.models import SchoolInformationOnBoarding
from StudentApp.models import Student
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


class StudentDetailInformationListSerializer(serializers.ModelSerializer):
    student_father_name_capital = serializers.CharField(source='father_name', read_only=True)
    student_mother_name_capital = serializers.CharField(source='mother_name', read_only=True)
    student_village_name = serializers.CharField(source='village_name', read_only=True)
    student_post_office_name = serializers.CharField(source='post_office_name', read_only=True)
    student_upazila_name = serializers.CharField(source='upazila_name', read_only=True)
    student_district_name = serializers.CharField(source='district_name', read_only=True)

    class Meta:
        model = Student
        fields = [
            "uid",
            "slug",
            "student_name_english_captial",
            "student_name_bangla",
            "phone",
            "nationality",
            "student_father_name_capital",
            "student_mother_name_capital",
            "student_village_name",
            "student_post_office_name",
            "student_upazila_name",
            "student_district_name",
        ]
        read_only_fields = ["uid", "slug", "phone", "student_name_bangla", "nationality",]



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
            'fees_collection_category',
            'school_fees_collection',
            'student_fees_collection'
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

class FeesCollectionDetailSerializer(serializers.ModelSerializer):
    fees_collection_category = FeesCategorySlimSerializer()
    school_fees_collection = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    student_fees_collection = StudentDetailInformationListSerializer()

    class Meta:
        model = FeesCollection
        fields = [
            "uid",
            "fees_amount",
            "paid_date",
            'fees_collection_category',
            'school_fees_collection',
            'student_fees_collection'
        ]
        read_only_fields = [
            "uid",
            'fees_collection_category',
            'school_fees_collection',
            'student_fees_collection'
        ]
