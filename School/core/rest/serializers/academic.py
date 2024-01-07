from rest_framework import serializers

from common.helpers import get_school_instance

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)
from core.models import (
    AcademicInformation,
)

from ...utills import (
    get_website_school_academic_homework_and_lecture_documents_pdf,
    get_website_school_academic_lesson_plan_documents_pdf,
    get_website_school_academic_calendar_documents_pdf,
    get_website_school_academic_syllabus_documents_pdf,
    get_website_school_academic_class_routine_documents_pdf
)

from core.choice import Status



class AcademicInformationCreateSerializer(serializers.Serializer):
    uid = serializers.UUIDField(format="hex_verbose", write_only=True)
    title = serializers.CharField(max_length=500, trim_whitespace=True)
    code_of_conducts = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Code of conducts",
        allow_blank=True,
    )
    guideline_for_parents = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Code of conducts",
        allow_blank=True,
    )
    dress_code = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Dress code",
        allow_blank=True,
    )
    homework_and_lecture_documents = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_homework_and_lecture_documents_pdf,
        label="Home work and lecture documents",
        required=False,) 
    lesson_plan = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_lesson_plan_documents_pdf,
        label="Lesson plan",
        required=False,) 
    academic_calendar = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_calendar_documents_pdf,
        label="Academic Calender",
        required=False,) 
    syllabus = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_syllabus_documents_pdf,
        label="Syllabus",
        required=False,) 
    class_routine = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_class_routine_documents_pdf,
        label="Class routine",
        required=False,) 
    co_curricular_activities = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Co curricula activities",
        allow_blank=True,
    )
    
    def validate(self, attrs):
        uid = attrs["uid"]
        school_instance = get_school_instance(uid)
        if not school_instance:
            raise serializers.ValidationError({"uid": "Invalid school UID."})

        return attrs

    def create(self, validated_data):
        uid = validated_data["uid"]
        title = validated_data["title"]
        code_of_conducts = validated_data["code_of_conducts"]
        guideline_for_parents = validated_data["guideline_for_parents"]
        dress_code = validated_data['dress_code']
        homework_and_lecture_documents = validated_data['homework_and_lecture_documents']
        lesson_plan = validated_data['lesson_plan']
        academic_calendar = validated_data['academic_calendar']
        syllabus = validated_data['syllabus']
        class_routine = validated_data['class_routine']
        co_curricular_activities = validated_data['co_curricular_activities']
        request = self.context["request"]
        user = request.user

        school_information_instance = get_school_instance(uid)
        
        academic = AcademicInformation.objects.create(
                school_academic_information_id=school_information_instance,
                title=title,
                code_of_conducts=code_of_conducts,
                guideline_for_parents=guideline_for_parents,
                dress_code=dress_code,
                homework_and_lecture_documents=homework_and_lecture_documents,
                lesson_plan=lesson_plan,
                academic_calendar=academic_calendar,
                syllabus=syllabus,
                class_routine=class_routine,
                co_curricular_activities=co_curricular_activities,
                user_created=user,
                status=Status.Active,
            )
        return academic


class AcademicInfoUpdateSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=500, trim_whitespace=True)
    code_of_conducts = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Code of conducts",
        allow_blank=True,
    )
    guideline_for_parents = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Code of conducts",
        allow_blank=True,
    )
    dress_code = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Dress code",
        allow_blank=True,
    )
    homework_and_lecture_documents = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_homework_and_lecture_documents_pdf,
        label="Home work and lecture documents",
        required=False,) 
    lesson_plan = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_lesson_plan_documents_pdf,
        label="Lesson plan",
        required=False,) 
    academic_calendar = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_calendar_documents_pdf,
        label="Academic Calender",
        required=False,) 
    syllabus = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_syllabus_documents_pdf,
        label="Syllabus",
        required=False,) 
    class_routine = serializers.FileField(max_length=None,
        allow_empty_file=False,
        use_url=get_website_school_academic_class_routine_documents_pdf,
        label="Class routine",
        required=False,) 
    co_curricular_activities = serializers.CharField(
        max_length=1000,
        trim_whitespace=True,
        required=False,
        label="Co curricula activities",
        allow_blank=True,
    )
    
   
    
    def update(self, instance, validated_data):
        
        request = self.context["request"]
        user = request.user

        instance.title = validated_data.get("title", instance.title)
        instance.code_of_conducts = validated_data.get("code_of_conducts", instance.code_of_conducts)
        instance.guideline_for_parents = validated_data.get("guideline_for_parents", instance.guideline_for_parents)
        instance.dress_code = validated_data.get("dress_code", instance.dress_code)
        instance.homework_and_lecture_documents = validated_data.get('homework_and_lecture_documents', instance.homework_and_lecture_documents)
        instance.lesson_plan = validated_data.get('lesson_plan', instance.lesson_plan)
        instance.academic_calendar = validated_data.get('academic_calendar', instance.academic_calendar)
        instance.syllabus = validated_data.get('syllabus', instance.syllabus)
        instance.class_routine = validated_data.get('class_routine', instance.class_routine)
        instance.co_curricular_activities = validated_data.get('co_curricular_activities', instance.co_curricular_activities)
        instance.user_updated = user
        instance.status = validated_data.get("status", instance.status)
        instance.save()

        return instance


class AcademicInformationListSerializer(serializers.ModelSerializer):
    school_academic_information = SchoolInformationOnBoardingListSerializer(
         many=False, read_only=True
    )

    class Meta:
        model = AcademicInformation
        fields = [
            "uid",
            "slug",
            "title",
            "code_of_conducts",
            "guideline_for_parents",
            "dress_code",
            "homework_and_lecture_documents",
            "lesson_plan",
            "academic_calendar",
            "syllabus",
            "class_routine",
            "co_curricular_activities",
            "school_academic_information",
        ]
