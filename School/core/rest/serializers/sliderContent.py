from rest_framework import serializers 
from django.core.validators import MinLengthValidator

from ...models import(
    WebsiteHomeSliderContent,
    WebsiteHomeSliderContentFile,

)

from ...helpers import (
    get_website_information_instance
    )

from ...utills import (
    get_website_home_slider_content_image,
)

from core.choice import (
    Status
)

from ..serializers import websiteInfo


class CreateWebsiteHomeSliderContentSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    title = serializers.CharField(max_length=30, trim_whitespace=True, required=False, label="Title", allow_blank=True)
    description = serializers.CharField(max_length=100, trim_whitespace=True, required=False, label="Short Description", allow_blank=True,  validators=[MinLengthValidator(11)])
    image = serializers.ImageField(max_length=None,allow_empty_file=False, use_url=get_website_home_slider_content_image, label="Image", required=False)


    def validate(self, attrs):
        
        uid = attrs['uid']
        website_home_slider_instance = get_website_information_instance(uid)
        if not website_home_slider_instance:
            raise serializers.ValidationError({"uid": "Invalid WebsiteInformation UID."})

        return attrs
    
    def create(self, validated_data):
        uid = validated_data['uid']
        title = validated_data['title']
        description = validated_data['description']
        image = validated_data['image']

        request = self.context['request']
        user = request.user


        website_home_slider_content_instance = get_website_information_instance(uid)

        sliderContent = WebsiteHomeSliderContent.objects.create(
                website_home_slider_content_id=website_home_slider_content_instance,
                title=title,
                description=description,
                user_created=user,
                status=Status.Active
                )

        school_contact = WebsiteHomeSliderContentFile.objects.create(
                home_content_id=sliderContent.id,
                image=image,
                user_created=user,
                status=Status.Active
                )

        return sliderContent
    


class SliderContentFileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteHomeSliderContentFile
        fields = ["uid", "image", "slug"]


class SliderContentListSerializer(serializers.ModelSerializer):
    websiteInfo = websiteInfo.WebsiteInformationSerializer(many=False, read_only=True, source='website_home_slider_content')
    file = SliderContentFileListSerializer(many=True, read_only=True, source='home_content_info')
    class Meta:
        model =  WebsiteHomeSliderContent
        fields = [
            'uid',
            'slug',
            'title',
            'description',
            'file',
            'websiteInfo'
        ]


class UpdateWebsiteHomeSliderContentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30, trim_whitespace=True, required=False, label="Title", allow_blank=True)
    description = serializers.CharField(max_length=100, trim_whitespace=True, required=False, label="Short Description", allow_blank=True, validators=[MinLengthValidator(11)])
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=get_website_home_slider_content_image, label="Image", required=False)

    def validate(self, data):
        title = data.get('title')
        description = data.get('description')

        if not title and not description:
            raise serializers.ValidationError("Either title or description must be provided.")

        return data

    def update(self, instance, validated_data):
        request = self.context["request"]
        user = request.user
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)
        
        instance.save()

        content_file_instance = WebsiteHomeSliderContentFile.objects.get(home_content=instance)

        if 'image' in validated_data:
            content_file_instance.image = validated_data['image']

        content_file_instance.user_updated = user
        content_file_instance.save()

        return instance
    
    def to_representation(self, instance):
        if self.context['request'].method == 'GET':
            return {
                'uid': str(instance.uid),
                'title': instance.title,
                'description': instance.description,
                'status': instance.status,
                'image': instance.home_content_info.first().image.url if instance.home_content_info.exists() else None,
            }
        
        return {
            'title': instance.title,
            'description': instance.description,
            'image': instance.home_content_info.first().image.url if instance.home_content_info.exists() else None,
           
        }
