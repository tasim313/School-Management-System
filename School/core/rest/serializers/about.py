from rest_framework import serializers

from ...models import (
    WebsiteAbout,
    WebsiteAboutFile,
    WebsiteFunFactContent,
    WebsiteAboutWinningAwards
)

from ...models import WebsiteAbout, WebsiteAboutFile
from common.models import SchoolInformationOnBoarding


class WebsiteAboutSerializer(serializers.ModelSerializer):
    
    website_about_content = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    
    class Meta:
        model = WebsiteAbout
        fields = [
            'uid',
            'slug',
            'title',
            'short_description',
            'long_description',
            'start_year',
            'vision',
            'mission',
            'website_about_content'
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



class WebsiteAboutFileSerializer(serializers.ModelSerializer):
    about = serializers.SlugRelatedField(
        queryset=WebsiteAbout.objects.all(),
        slug_field="uid",
    )
    class Meta:
        model = WebsiteAboutFile
        fields = (
            'uid',
            'slug',
            'image',
            'about'
        )
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
    


class WebsiteFunFactContentSerializer(serializers.ModelSerializer):
    about_info = serializers.SlugRelatedField(
        queryset=WebsiteAbout.objects.all(),
        slug_field="uid",
    )
    class Meta:
        model = WebsiteFunFactContent
        fields = (
            'uid',
            'number_of_students',
            'number_of_alumni',
            'winning_awards',
            "years_of_experience",
            'about_info'
        )
        read_only_fields = ["uid", "years_of_experience"]

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



class WebsiteAboutWinningAwardsSerializer(serializers.ModelSerializer):
    school_award = serializers.SlugRelatedField(
        queryset=WebsiteAbout.objects.all(),
        slug_field="uid",
    )
    class Meta:
        model = WebsiteAboutWinningAwards
        fields = (
            'uid',
            'title',
            'awards_image',
            'school_award'
        )



class AboutListSerializer(serializers.Serializer):
    website_about = WebsiteAboutSerializer()
    website_about_file = WebsiteAboutFileSerializer(many=True)
    website_fun_fact_content = WebsiteFunFactContentSerializer()
    website_about_winning_awards = WebsiteAboutWinningAwardsSerializer()

    def to_representation(self, instance):
        initial_representation = super().to_representation(instance)
        filtered_representation = {key: value for key, value in initial_representation.items() if value is not None}
        return filtered_representation