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

from common.rest.serializers import schoolInformation

import logging

logger = logging.getLogger(__name__)


class SchoolWebsiteLiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebsiteInformation
        fields = [
            "id",
            "slug",
            "name",
            "logo",
        ]


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
    
    def validate(self, attrs):
        
        uid = attrs['uid']
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs
    
    def create(self, validated_data):
        uid = validated_data['uid']
        name = validated_data['name']
        logo = validated_data['logo']
        favicon = validated_data['favicon']

        request = self.context['request']
        user = request.user

        school_information_instance = get_school_instance(uid)
        website_obj = WebsiteInformation.objects.filter(school_website=school_information_instance).count()

        if website_obj > 0:
                        msg = 'Access denied: You cannot create new Website Information. Please update previous information or delete previous data.'
                        raise serializers.ValidationError(msg)

        else:
                website = WebsiteInformation.objects.create(
                school_website_id=school_information_instance,
                name=name,
                logo=logo,
                favicon=favicon,
                user_created=user,
                status=Status.Active
                )

                school_address = SchoolAddressInformation.objects.create(
                school_address_id=website.id,
                divisions=validated_data.get('divisions'),
                district=validated_data.get('district'),
                upazila=validated_data.get('upazila'),
                pourashava=validated_data.get('pourashava'),
                union_parishad=validated_data.get('union_parishad'),
                ward=validated_data.get('ward'),
                mouza=validated_data.get('mouza'),
                village=validated_data.get('village'),
                house_holding_number=validated_data.get('house_holding_number'),
                post_office=validated_data.get('post_office'),
                post_code=validated_data.get('post_code')
                )

                school_contact = SchoolContactInformation.objects.create(
                school_contact_id=website.id,
                school_contact_address_id=school_address.id,
                phone=validated_data.get('phone'),
                email=validated_data.get('email')
                )

                return website




class SchoolContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolContactInformation
        fields = ["uid", "phone", "email", "slug"]




class SchoolAddressInformationSerializer(serializers.ModelSerializer):
    school_contact_address = SchoolContactInformationSerializer(many=True, read_only=True)

    class Meta:
        model = SchoolAddressInformation
        fields = [
            'uid', 'slug', 'divisions', "district", "upazila", "pourashava", 
            "union_parishad", "ward", "mouza", "village", "house_holding_number", 
            "post_office", "post_code", "school_contact_address"
        ]



class WebsiteInformationSerializer(serializers.ModelSerializer):
    school_address_information = SchoolAddressInformationSerializer(many=True, read_only=True)
    school_website = schoolInformation.SchoolInformationOnBoardingListSerializer(many=False, read_only=True)

    class Meta:
        model = WebsiteInformation 
        fields = ['uid', 'name', 'logo', 'favicon', 'slug',"school_website",'school_address_information']



class SchoolWebsiteUpdateSerializer(serializers.Serializer):
    
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
        status = serializers.ChoiceField(choices=Status.choices, required=False, label="Status")
 
        
        def validate(self, attrs):
        
                uid = attrs['uid']
                school_instance = get_school_instance(uid)
                if not school_instance:
                    raise serializers.ValidationError({"uid": "Invalid school UID."})

                return attrs

        def update(self, instance, validated_data):
                """
                Update and return an existing `WebsiteInformation` instance,
                given the validated data.
                """
                request = self.context['request']
                user = request.user
                
                instance.name = validated_data.get('name', instance.name)
                instance.logo = validated_data.get('logo', instance.logo)
                instance.favicon = validated_data.get('favicon', instance.favicon)
                instance.user_updated = user
                instance.status = validated_data.get('status', instance.status)

                # Update SchoolAddressInformation related to the website
                school_address = SchoolAddressInformation.objects.get(school_address=instance)
                school_address.divisions = validated_data.get('divisions', school_address.divisions)
                school_address.district = validated_data.get('district', school_address.district)
                school_address.upazila = validated_data.get('upazila', school_address.upazila)
                school_address.pourashava = validated_data.get('pourashava', school_address.pourashava)
                school_address.union_parishad = validated_data.get('union_parishad', school_address.union_parishad)
                school_address.ward = validated_data.get('ward', school_address.ward)
                school_address.mouza = validated_data.get('mouza', school_address.mouza)
                school_address.village = validated_data.get('village', school_address.village)
                school_address.house_holding_number = validated_data.get('house_holding_number', school_address.house_holding_number)
                school_address.post_office = validated_data.get('post_office', school_address.post_office)
                school_address.post_code = validated_data.get('post_code', school_address.post_code)
                school_address.user_updated = user
                school_address.save()

                # Update SchoolContactInformation related to the website
                school_contact = SchoolContactInformation.objects.get(school_contact=instance)
                school_contact.phone = validated_data.get('phone', school_contact.phone)
                school_contact.email = validated_data.get('email', school_contact.email)
                school_contact.user_updated = user
                school_contact.save()

                # Save the changes to the website instance
                instance.save()

                return instance
