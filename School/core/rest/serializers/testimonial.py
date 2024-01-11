from rest_framework import serializers

from common.helpers import get_school_instance

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)
from core.models import (
    Testimonials,
)

from ...utills import (
  get_testimonials_image
)

from core.choice import Status




class TestimonialsCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    name = serializers.CharField(max_length=255, trim_whitespace=True, label="Name")
    designation = serializers.CharField(
        max_length=500,
        trim_whitespace=True,
        required=False,
        label="Designation",
        allow_blank=True,
    )
    comment = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Comment",
        allow_blank=True,
    )
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False, 
        use_url=get_testimonials_image, 
        label="Image", 
        required=False)
    
    
    def validate(self, attrs):
        uid = attrs["uid"]
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        uid = validated_data["uid"]
        name = validated_data["name"]
        designation = validated_data["designation"]
        comment = validated_data["comment"]
        image = validated_data['image']
        
        request = self.context["request"]
        user = request.user

        school_information_instance = get_school_instance(uid)
        
        testimonial = Testimonials.objects.create(
                school_testimonials_id=school_information_instance,
                name=name,
                designation=designation,
                comment=comment,
                image=image,
                user_created=user,
                status=Status.Active,
            )
        return testimonial


class TestimonialsUpdateSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=255, trim_whitespace=True, label="Name")
    designation = serializers.CharField(
        max_length=500,
        trim_whitespace=True,
        required=False,
        label="Designation",
        allow_blank=True,
    )
    comment = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Comment",
        allow_blank=True,
    )
    image = serializers.ImageField(
        max_length=None,
        allow_empty_file=False, 
        use_url=get_testimonials_image, 
        label="Image", 
        required=False)
    
   
    
    def update(self, instance, validated_data):
        
        request = self.context["request"]
        user = request.user

        instance.name = validated_data.get("name", instance.name)
        instance.designation = validated_data.get("designation", instance.designation)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.image = validated_data.get("image", instance.image)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance


class TestimonialsListSerializer(serializers.ModelSerializer):
    school_testimonials = SchoolInformationOnBoardingListSerializer(
         many=False, read_only=True
    )

    class Meta:
        model = Testimonials
        fields = [
            "uid",
            "slug",
            "name",
            "designation",
            "comment",
            "image",
            "school_testimonials",
        ]
