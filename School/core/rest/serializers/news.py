from rest_framework import serializers
from django.core.validators import MinLengthValidator


from core.models import NewsEvents

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)

from common.helpers import get_school_instance

from core.choice import(
    NewsEventsStatus,
    Status
)

from ...utills import (
    get_news_events_image,
)


class NewsEventCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    headline = serializers.CharField(max_length=300, trim_whitespace=True, label = "Title")
    news_events_status = serializers.ChoiceField(
        choices= NewsEventsStatus.choices,
        required=False, allow_blank=True, 
        label = "News events status"
    )
    description = serializers.CharField(
        max_length=1000, 
        trim_whitespace=True, 
        required=False, 
        label="Description", 
        allow_blank=True,
        validators=[MinLengthValidator(11)])
    publish_date = serializers.DateTimeField(
        required=False,
        label="Publish Date"
    )
    image = serializers.ImageField(max_length=None,allow_empty_file=False, use_url=get_news_events_image, label="Image", required=False)
    
    
    def validate(self, attrs):
        uid = attrs["uid"]
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        uid = validated_data["uid"]
        headline = validated_data["headline"]
        news_events_status = validated_data["news_events_status"]
        description = validated_data["description"]
        publish_date = validated_data['publish_date']
        image = validated_data['image']
        request = self.context["request"]
        user = request.user

        school_information_instance = get_school_instance(uid)
        
        news_events = NewsEvents.objects.create(
                school_id=school_information_instance,
                headline=headline,
                news_events_status=news_events_status,
                description=description,
                publish_date=publish_date,
                image=image,
                user_created=user,
                status=Status.Active,
            )
        return news_events


class NewsEventUpdateSerializer(serializers.Serializer):
    
    headline = serializers.CharField(max_length=300, trim_whitespace=True, label = "Title")
    news_events_status = serializers.ChoiceField(
        choices= NewsEventsStatus.choices,
        required=False, allow_blank=True, 
        label = "News events status"
    )
    description = serializers.CharField(
        max_length=1000, 
        trim_whitespace=True, 
        required=False, 
        label="Description", 
        allow_blank=True,
        validators=[MinLengthValidator(11)])
    publish_date = serializers.DateTimeField(
        required=False,
        label="Publish Date"
    )
    image = serializers.ImageField(max_length=None,allow_empty_file=False, use_url=get_news_events_image, label="Image", required=False)
    
   
    
    def update(self, instance, validated_data):
        
        request = self.context["request"]
        user = request.user

        instance.headline = validated_data.get("headline", instance.headline)
        instance.news_events_status = validated_data.get("news_events_status", instance.news_events_status)
        instance.description = validated_data.get("description", instance.description)
        instance.publish_date = validated_data.get("publish_date", instance.publish_date)
        instance.image = validated_data.get('image', instance.image)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance


class NewsEventListSerializer(serializers.ModelSerializer):
    school = SchoolInformationOnBoardingListSerializer(
         many=False, read_only=True
    )

    class Meta:
        model = NewsEvents
        fields = [
            "uid",
            "slug",
            "news_events_status",
            "headline",
            "description",
            "publish_date",
            "image",
            'school'
        ]
