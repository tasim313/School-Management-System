from rest_framework import serializers

from ...models import (
    WebsiteAbout,
    WebsiteAboutFile,
    WebsiteFunFactContent,
    WebsiteAboutWinningAwards
)

from core.choice import Status

from common.helpers import get_school_instance
from ...helpers import  get_website_about
from ...models import WebsiteAbout, WebsiteAboutFile
from ..serializers import websiteInfo



class WebsiteAboutWinningAwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteAboutWinningAwards
        fields = (
            'uid',
            'title',
            'awards_image'
        )

class WebsiteFunFactContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteFunFactContent
        fields = (
            'uid',
            'number_of_students',
            'number_of_alumni',
            'winning_awards',
            'years_of_experience'
        )

class WebsiteAboutFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteAboutFile
        fields = (
            'uid',
            'slug',
            'image'
        )


class WebsiteAboutSerializer(serializers.ModelSerializer):
    about = WebsiteAboutFileSerializer(many=False)
    about_info = WebsiteFunFactContentSerializer(many=False)
    school_award = WebsiteAboutWinningAwardsSerializer(many=False)

    class Meta:
        model = WebsiteAbout
        fields = (
            'uid',
            'slug',
            'title',
            'short_description',
            'long_description',
            'start_year',
            'vision',
            'mission'
            
        )

    def validate(self, attrs):
        uid = attrs.get("uid")
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        
        if WebsiteAbout.objects.filter(website_about_content=school_instance).exists():
            raise serializers.ValidationError("Data already exists for this school.")

        return attrs

    def create(self, validated_data):
        website_about_file_data = validated_data.pop('about', [])
        about_fun_fact_data = validated_data.pop('about_info', [])
        school_award_data = validated_data.pop('school_award', [])

        website_about = WebsiteAbout.objects.create(**validated_data)

        for about_file in website_about_file_data:
            WebsiteAboutFile.objects.create(about=website_about, **about_file)

        for fun_fact in about_fun_fact_data:
            WebsiteFunFactContent.objects.create(about_info=website_about, **fun_fact)

        for award in school_award_data:
            WebsiteAboutWinningAwards.objects.create(school_award=website_about, **award)

        return website_about