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


class SocialMediaCreateSerializer(serializers.Serializer):

    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
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
    

    def validate(self, attrs):
        uid = attrs["uid"]
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs
    

    def create(self, validated_data):
        uid = validated_data['uid']
        facebook_url = validated_data['facebook_url']
        twitter_url = validated_data['twitter_url']
        instagram_url = validated_data['instagram_url']
        linkedin_url = validated_data['linkedin_url']

        request = self.context['request']
        user = request.user


        school_social_media_instance = get_school_instance(uid)

        social_media = SocialMedia.objects.create(
                school_social_media_id=school_social_media_instance,
                facebook_url=facebook_url,
                twitter_url=twitter_url,
                instagram_url=instagram_url,
                linkedin_url=linkedin_url,
                user_created=user,
                status=Status.Active
                )
        return social_media
    

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