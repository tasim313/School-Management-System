from rest_framework import serializers
from core.models import SchoolClass

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)

from common.helpers import get_school_instance

from core.choice import(
    Status
)


class SchoolClassCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    name = serializers.CharField(max_length=100, trim_whitespace=True, label = "Class Name")
    
    def validate(self, attrs):
        uid = attrs["uid"]
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        uid = validated_data["uid"]
        name = validated_data["name"]
        request = self.context["request"]
        user = request.user
        
        school_information_instance = get_school_instance(uid)
        
        school_class = SchoolClass.objects.create(
                school_info_id=school_information_instance,
                name=name,
                user_created=user,
                status=Status.Active,
            )
        return school_class


class SchoolClassUpdateSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100, trim_whitespace=True, label = "Class Name")
    
    def update(self, instance, validated_data):
        
        request = self.context["request"]
        user = request.user

        instance.name = validated_data.get("name", instance.name)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance


class SchoolClassListSerializer(serializers.ModelSerializer):
    school_info = SchoolInformationOnBoardingListSerializer(
         many=False, read_only=True
    )

    class Meta:
        model = SchoolClass
        fields = [
            "uid",
            "slug",
            "name",
            'school_info'
        ]
