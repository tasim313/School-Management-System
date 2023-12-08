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