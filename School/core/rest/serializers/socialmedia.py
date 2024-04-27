from rest_framework import serializers 

from ...models import(
    SocialMedia
)

from common.helpers import get_school_instance

from core.choice import (
    Status
)

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)

from common.models import SchoolInformationOnBoarding


class SocialMediaCreateSerializer(serializers.ModelSerializer):

    school_social_media = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = SocialMedia
        fields = [
            "uid",
            "slug",
            "school_social_media",
            "facebook_url",
            "twitter_url",
            "instagram_url",
            "linkedin_url",
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance

    


class SocialMediaUpdateSerializer(serializers.Serializer):

    facebook_url = serializers.URLField(max_length=None,
        allow_blank=True,
        label="Facebook url",
        required=False,) 
    twitter_url = serializers.URLField(max_length=None,
        allow_blank=True,
        label="Twitter url",
        required=False,) 
    instagram_url = serializers.URLField(max_length=None,
        allow_blank=True,
        label="Instagram url",
        required=False,) 
    linkedin_url = serializers.URLField(max_length=None,
        allow_blank=True,
        label="Linkedin url",
        required=False,) 

    def update(self, instance, validated_data):
        request = self.context["request"]
        user = request.user
        instance.facebook_url = validated_data.get('facebook_url', instance.facebook_url)
        instance.twitter_url = validated_data.get('twitter_url', instance.twitter_url)
        instance.instagram_url = validated_data.get('instagram_url', instance.instagram_url)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)

        instance.save()


class SocialMediaListSerializer(serializers.ModelSerializer):
    school_social_media = SchoolInformationOnBoardingListSerializer(
         many=False, read_only=True
    )
    class Meta:
        model = SocialMedia
        fields = ["uid",  "slug", 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'school_social_media']