from rest_framework import serializers

from core.models import SchoolAdmission

from common.helpers import get_school_instance

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)

from ...utills import (
    get_website_school_admission_pdf,
)

from core.choice import(
    AdmissionClass,
    AdmissionBranch,
    AdmissionDivision,
    Status
)


class AdmissionCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    title = serializers.CharField(max_length=500, trim_whitespace=True)
    admission_class = serializers.ChoiceField(
        choices=AdmissionClass.choices,
        required=False, allow_blank=True, 
        label = "Admission class"
    )
    admission_branch = serializers.ChoiceField(
        choices=AdmissionBranch.choices,
        required=False, allow_blank=True, 
        label = "Admission branch"
    )
    admission_division = serializers.ChoiceField(
        choices=AdmissionDivision.choices,
        required=False, allow_blank=True, 
        label = "Admission division"
    )
    number_of_seats = serializers.CharField(
        max_length=100,
        trim_whitespace=True,
        required=False,
        label="Number of seats",
        allow_blank=True,
    )
    limit_of_age = serializers.CharField(
        max_length=100,
        trim_whitespace=True,
        required=False,
        label="Limit of age",
        allow_blank=True,
    )
    collection_of_prospectus = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Collection of prospectus",
        allow_blank=True,
    )
    fill_the_application_form = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Fill the application form",
        allow_blank=True,
    )
    online_admission_form_date_time = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Online admission form date time",
        allow_blank=True,
    )
    admission_process_college_information_website = serializers.URLField(max_length=None,
        allow_blank=True,
        label="School website url link",
        required=False,) 
    digital_lottery_time_information = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Digital lottery time information",
        allow_blank=True,
    )
    admission_application_rules = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Admission application rules",
        allow_blank=True,
    )
    other_description = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Other description",
        allow_blank=True,
    )
    remark = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Remark",
        allow_blank=True,
    )
    pdf_file = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_admission_pdf,
        label="Pdf file",
        required=False,) 

    
    
    def validate(self, attrs):
        uid = attrs["uid"]
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        uid = validated_data["uid"]
        title = validated_data["title"]
        admission_class = validated_data["admission_class"]
        admission_branch = validated_data["admission_branch"]
        admission_division = validated_data['admission_division']
        number_of_seats = validated_data['number_of_seats']
        limit_of_age = validated_data['limit_of_age']
        collection_of_prospectus = validated_data['collection_of_prospectus']
        fill_the_application_form = validated_data['fill_the_application_form']
        online_admission_form_date_time = validated_data['online_admission_form_date_time']
        admission_process_college_information_website = validated_data['admission_process_college_information_website']
        digital_lottery_time_information = validated_data['digital_lottery_time_information']
        admission_application_rules = validated_data['admission_application_rules']
        other_description = validated_data['other_description']
        remark = validated_data['remark']
        pdf_file = validated_data['pdf_file']
        request = self.context["request"]
        user = request.user

        school_information_instance = get_school_instance(uid)
        
        admission = SchoolAdmission.objects.create(
                school_admission_id=school_information_instance,
                title=title,
                admission_class=admission_class,
                admission_branch=admission_branch,
                admission_division=admission_division,
                number_of_seats=number_of_seats,
                limit_of_age=limit_of_age,
                collection_of_prospectus=collection_of_prospectus,
                fill_the_application_form=fill_the_application_form,
                online_admission_form_date_time=online_admission_form_date_time,
                admission_process_college_information_website=admission_process_college_information_website,
                digital_lottery_time_information = digital_lottery_time_information,
                admission_application_rules = admission_application_rules,
                other_description = other_description,
                remark = remark,
                pdf_file = pdf_file,
                user_created=user,
                status=Status.Active,
            )
        return admission


class AdmissionUpdateSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=500, trim_whitespace=True)
    admission_class = serializers.ChoiceField(
        choices=AdmissionClass.choices,
        required=False, allow_blank=True, 
        label = "Admission class"
    )
    admission_branch = serializers.ChoiceField(
        choices=AdmissionBranch.choices,
        required=False, allow_blank=True, 
        label = "Admission branch"
    )
    admission_division = serializers.ChoiceField(
        choices=AdmissionDivision.choices,
        required=False, allow_blank=True, 
        label = "Admission division"
    )
    number_of_seats = serializers.CharField(
        max_length=100,
        trim_whitespace=True,
        required=False,
        label="Number of seats",
        allow_blank=True,
    )
    limit_of_age = serializers.CharField(
        max_length=100,
        trim_whitespace=True,
        required=False,
        label="Limit of age",
        allow_blank=True,
    )
    collection_of_prospectus = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Collection of prospectus",
        allow_blank=True,
    )
    fill_the_application_form = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Fill the application form",
        allow_blank=True,
    )
    online_admission_form_date_time = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Online admission form date time",
        allow_blank=True,
    )
    admission_process_college_information_website = serializers.URLField(max_length=None,
        allow_blank=True,
        label="School website url link",
        required=False,) 
    digital_lottery_time_information = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Digital lottery time information",
        allow_blank=True,
    )
    admission_application_rules = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Admission application rules",
        allow_blank=True,
    )
    other_description = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Other description",
        allow_blank=True,
    )
    remark = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Remark",
        allow_blank=True,
    )
    pdf_file = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_admission_pdf,
        label="Pdf file",
        required=False,) 
    
   
    
    def update(self, instance, validated_data):
        
        request = self.context["request"]
        user = request.user

        instance.title = validated_data.get("title", instance.title)
        instance.admission_class = validated_data.get("admission_class", instance.admission_class)
        instance.admission_branch = validated_data.get("admission_branch", instance.admission_branch)
        instance.admission_division = validated_data.get("admission_division", instance.admission_division)
        instance.number_of_seats = validated_data.get('number_of_seats', instance.number_of_seats)
        instance.limit_of_age = validated_data.get('limit_of_age', instance.limit_of_age)
        instance.collection_of_prospectus = validated_data.get('collection_of_prospectus', instance.collection_of_prospectus)
        instance.fill_the_application_form = validated_data.get('fill_the_application_form', instance.fill_the_application_form)
        instance.online_admission_form_date_time = validated_data.get('online_admission_form_date_time', instance.online_admission_form_date_time)
        instance.admission_process_college_information_website = validated_data.get('admission_process_college_information_website', instance.admission_process_college_information_website)
        instance.digital_lottery_time_information = validated_data.get('digital_lottery_time_information', instance.digital_lottery_time_information)
        instance.admission_application_rules = validated_data.get('admission_application_rules', instance.admission_application_rules)
        instance.other_description = validated_data.get('other_description', instance.other_description)
        instance.remark = validated_data.get('remark', instance.remark)
        instance.pdf_file = validated_data.get('pdf_file', instance.pdf_file)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance


class AdmissionListSerializer(serializers.ModelSerializer):
    school_admission = SchoolInformationOnBoardingListSerializer(
         many=False, read_only=True
    )

    class Meta:
        model = SchoolAdmission
        fields = [
            "uid",
            "slug",
            "title",
            "admission_class",
            "admission_branch",
            "admission_division",
            "number_of_seats",
            "limit_of_age",
            "collection_of_prospectus",
            "fill_the_application_form",
            "online_admission_form_date_time",
            "admission_process_college_information_website",
            "digital_lottery_time_information",
            "admission_application_rules",
            "other_description",
            "remark",
            "pdf_file",
            "school_admission"
        ]
