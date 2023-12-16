from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.core.validators import ValidationError

from ...models import SchoolInformationOnBoarding
from ...choice import SchoolType

import logging

logger = logging.getLogger(__name__)


class SchoolInformationOnBoardingCreateSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255, label="School Name", trim_whitespace=True, required=True
    )
    address = serializers.CharField(
        max_length=550, label="School Address", trim_whitespace=True, required=True
    )
    phone = PhoneNumberField(label="School Phone Number or Contact Number")
    school_type = serializers.ChoiceField(
        label="Chose School User Size", choices=SchoolType.choices
    )

    class Meta:
        fields = ("name", "address", "phone", "school_type")

    def validate_phone(self, value):
        phone_field = PhoneNumberField()
        try:
            validated_phone = phone_field.to_internal_value(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.detail)

        return validated_phone

    def create(self, validated_data, *args, **kwargs):
        name = validated_data["name"]
        address = validated_data["address"]
        phone = validated_data["phone"]

        school_information = SchoolInformationOnBoarding.objects.create(
            name=name,
            address=address,
            phone=phone,
            school_type=validated_data["school_type"],
        )

        logger.debug(
            f"New School Information OnBoard in our Application: {school_information}"
        )

        return school_information


class SchoolInformationOnBoardingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInformationOnBoarding
        fields = (
            "uid",
            "name",
            "address",
            "phone",
            "school_type",
            "slug",
        )


class SchoolInformationOnBoardingUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=255, label="School Name", trim_whitespace=True, required=False
    )
    address = serializers.CharField(
        max_length=550, label="School Address", trim_whitespace=True, required=False
    )
    phone = PhoneNumberField(
        label="School Phone Number or Contact Number", required=False
    )
    school_type = serializers.ChoiceField(
        label="Chose School User Size", choices=SchoolType.choices, required=False
    )

    class Meta:
        fields = ("name", "address", "phone", "school_type")

    def validate_phone(self, value):
        phone_field = PhoneNumberField()
        try:
            validated_phone = phone_field.to_internal_value(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.detail)

        return validated_phone

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.school_type = validated_data.get("school_type", instance.school_type)
        instance.save()

        logger.debug(
            f"Updated School Information OnBoard in our Application: {instance}"
        )

        return instance
