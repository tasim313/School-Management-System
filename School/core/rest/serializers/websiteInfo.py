from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from phonenumber_field.serializerfields import PhoneNumberField


from ...models import (
    WebsiteInformation,
    SchoolAddressInformation,
    SchoolContactInformation
)

from common.helpers import get_school_instance
from core.choice import (
    Status
)

from ...utills import(
    get_school_website_logo,
    get_school_website_favicon,
)

import logging

logger = logging.getLogger(__name__)




class SchoolWebsiteCreateSerializer(serializers.Serializer):

    uid = serializers.UUIDField(format='hex_verbose', write_only=True)
    name = serializers.CharField(
        max_length=255,
        trim_whitespace=True)
    logo = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_school_website_logo,
                                     label="School Logo",
                                     required=False)
    favicon = serializers.ImageField(max_length=None,
                                     allow_empty_file=False,
                                     use_url=get_school_website_favicon,
                                     label="Favicon Icon",
                                     required=False)
    divisions = serializers.CharField(max_length=255,
                                        trim_whitespace=True, required=False,
            label="Divisions",
            allow_blank=True,)
    district = serializers.CharField(max_length=255,
                                        trim_whitespace=True, required=False,
            label="District",
            allow_blank=True,)
    upazila  = serializers.CharField(max_length=255,
                                        trim_whitespace=True,
                                        required=False, label="Upazila", allow_blank=True,)
    pourashava = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label="Pourashava",
            allow_blank=True,)
    union_parishad = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label="Union Parishad",
            allow_blank=True,)
    ward = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label="Ward",
            allow_blank=True,)
    mouza = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label="Mouza",
            allow_blank=True,)
    village = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label="Village",
            allow_blank=True,)
    house_holding_number = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label=" House Holding Number",
            allow_blank=True,)
    post_office = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label=" Post Office",
            allow_blank=True,)
    post_code = serializers.CharField(max_length=255, trim_whitespace=True, required=False,
            label=" Post Code",
            allow_blank=True,)
    phone  = PhoneNumberField(required=False,  allow_blank=True, label="School Website Phone Number or Contact Number")
    email = serializers.EmailField(
            required=False,
            label=" Email Address",
            allow_blank=True,
            )   

    def create(self, validated_data):

        uid = validated_data['uid']
        name = validated_data['name']
        logo = validated_data['logo']
        favicon = validated_data['favicon']

        request = self.context['request']
        user = request.user
        
        website_obj = WebsiteInformation.objects.all().count()

        school_information_instance = get_school_instance(uid)

        if website_obj > 0:
            msg = 'Access denied: You Can not create new Website Information, Please update previous information or delete previous data'
            raise serializers.ValidationError(msg)
            
        else:
                website = WebsiteInformation.objects.create(
                        school_website_id = school_information_instance,
                        name=name,
                        logo=logo,
                        favicon=favicon,
                        user_created= user,
                        status=Status.Active
                        )

                school_address = SchoolAddressInformation.objects.create(
                        school_address_id = website.id,
                        divisions = validated_data.get('divisions'),
                        district = validated_data.get('district'),
                        upazila = validated_data.get('upazila'),
                        pourashava = validated_data.get('pourashava'),
                        union_parishad = validated_data.get('union_parishad'),
                        ward = validated_data.get('ward'),
                        mouza = validated_data.get('mouza'),
                        village = validated_data.get('village'),
                        house_holding_number = validated_data.get('house_holding_number'),
                        post_office = validated_data.get('post_office'),
                        post_code = validated_data.get('post_code')

                        )
                
                school_contact = SchoolContactInformation.objects.create(
                        school_contact_id = website.id,
                        school_contact_address_id = school_address.id,
                        phone = validated_data.get('phone'),
                        email = validated_data.get('email')
                )
            
        return website