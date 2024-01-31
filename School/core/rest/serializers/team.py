from rest_framework import serializers

from core.models import (
    WebsiteTeacherInformation, 
    WebsiteManagingCommitteeMemberInformation, 
    WebsiteStaffInformation, 
    WebSiteFacultyInformation
    )
from common.models import SchoolInformationOnBoarding



class WebsiteTeacherInformationListSerializer(serializers.ModelSerializer):
    
    school_teacher = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = WebsiteTeacherInformation
        fields = [
            "uid",
            "slug",
            "first_name",
            "last_name",
            "position",
            'bio',
            'contact_email',
            'contact_phone',
            'school_teacher',
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



class WebsiteManagingCommitteeMemberInformationListSerializer(serializers.ModelSerializer):
    
    school_managing_committee_member = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = WebsiteManagingCommitteeMemberInformation
        fields = [
            "uid",
            "slug",
            "first_name",
            "last_name",
            "position",
            "bio",
            "contact_email",
            "contact_phone",
            'school_managing_committee_member',
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



class WebsiteStaffInformationListSerializer(serializers.ModelSerializer):
    
    school_staff = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = WebsiteStaffInformation
        fields = [
            "uid",
            "slug",
            "first_name",
            "last_name",
            "position",
            "bio",
            "contact_email",
            "contact_phone",
            'school_staff',
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



class  WebSiteFacultyInformationListSerializer(serializers.ModelSerializer):
    
    school_faculty = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    teachers = serializers.SlugRelatedField(
        queryset=WebsiteTeacherInformation.objects.all(),
        slug_field="uid",
        many = True,
        allow_null = True,
        required = False
    )

    staff_members = serializers.SlugRelatedField(
        queryset=WebsiteStaffInformation.objects.all(),
        slug_field="uid",
        many = True,
        allow_null = True,
        required = False
    )

    managing_committee_member = serializers.SlugRelatedField(
        queryset=WebsiteManagingCommitteeMemberInformation.objects.all(),
        slug_field="uid",
        many = True,
        allow_null = True,
        required = False
    )

    class Meta:
        model = WebSiteFacultyInformation
        fields = [
            "uid",
            "slug",
            "school_faculty",
            "teachers",
            "staff_members",
            "managing_committee_member"
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