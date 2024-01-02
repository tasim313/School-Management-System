from rest_framework import serializers

from ...models import (
    WebsiteAbout,
    WebsiteAboutFile,
)

from core.choice import Status

from ...helpers import get_website_information_instance , get_website_about
from ...models import WebsiteAbout, WebsiteAboutFile
from ..serializers import websiteInfo
from ...utills import(
    get_website_about_file_image
)

class SchoolAboutInformationCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    title = serializers.CharField(max_length=200, trim_whitespace=True)
    short_description = serializers.CharField(max_length=1000, trim_whitespace=True)
    long_description = serializers.CharField(max_length=1000, trim_whitespace=True)
    start_year = serializers.DateField()
    vision =  serializers.CharField(max_length=1000, trim_whitespace=True)
    mission = serializers.CharField(max_length=1000, trim_whitespace=True)

    class Meta:
        model = WebsiteAbout
        fields = (
            'uid',
            'title',
            'short_description',
            'support_description',
            'start_year',
            'vision',
            'mission',
        )

    def validate(self, attrs):
        uid = attrs["uid"]
        website_instance = get_website_information_instance(uid)
        if not website_instance:
            raise serializers.ValidationError({"uid": "Invalid website UID."})

        return attrs


    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        uid = validated_data["uid"]
        title = validated_data['title']
        short_description = validated_data['short_description']
        long_description = validated_data['long_description']
        start_year = validated_data['start_year']
        vision = validated_data['vision']
        mission = validated_data['mission']
        about_obj = WebsiteAbout.objects.all().count()

        website_instance = get_website_information_instance(uid)

        if about_obj > 0:
            msg = 'Access denied: You Can not create new About Information, Please update previous information or delete previous data'
            raise serializers.ValidationError(msg)
        
            
        else:
            about = WebsiteAbout.objects.create(
                        website_about_content_id = website_instance,
                        title=title,
                        short_description=short_description,
                        long_description=long_description,
                        start_year=start_year,
                        vision=vision,
                        mission=mission,
                        user_created=user,
                        status=Status.Active
                        )
            
        return about



class SchoolAboutInformationList(serializers.ModelSerializer):
    website_about_content = websiteInfo.WebsiteInformationSerializer(
        many=False, read_only=True
    )
    class Meta:
        model = WebsiteAbout
        fields = [
            'uid',
            'title',
            'short_description',
            'long_description',
            'start_year',
            'vision',
            'mission',
            'website_about_content'
        ]


class SchoolAboutFileCreate(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False,
        use_url=get_website_about_file_image,
        label="Image",
        required=False,
    )

    def validate(self, attrs):
        uid = attrs["uid"]
        about_instance = get_website_about(uid)
        if not about_instance:
            raise serializers.ValidationError({"uid": "Invalid website about UID."})

        return attrs
    

    def create(self, validated_data):
        request = self.context['request']
        user = request.user

        uid = validated_data["uid"]
        image = validated_data['image']
        
        about_instance = get_website_about(uid)
        
        about = WebsiteAboutFile.objects.create(
                about_id = about_instance,
                image=image,
                user_created=user,
                status=Status.Active
        )
            
        return about
    

class SchoolAboutFileList(serializers.ModelSerializer):
    about = SchoolAboutInformationList(
        many=False, read_only=True
    )

    class Meta:
        model = WebsiteAboutFile
        fields = [
            'uid',
            'slug',
            'image',
            'status',
            'user_created',
            'user_updated',
            'about'
        ]