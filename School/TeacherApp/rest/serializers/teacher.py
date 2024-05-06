from rest_framework import serializers
from school_auth.rest.serializers.UserSerializer import UserSerializer
from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingCreateSerializer,
)
from TeacherApp.models import Teacher, TeacherImage

from core.models import User
from common.models import SchoolInformationOnBoarding


class TeacherImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherImage
        fields = [
            "uid",
            "teacher_info",
            "slug",
            "image",
        ]


class TeacherListDetailSerializer(serializers.ModelSerializer):
    teacher_information = TeacherImageSerializer(many=True, read_only=True)
    teacher_user = UserSerializer()
    school_teacher = SchoolInformationOnBoardingCreateSerializer()

    class Meta:
        model = Teacher
        fields = [
            "uid",
            "slug",
            "school_teacher",
            "teacher_user",
            "teacher_id",
            "name",
            "gender",
            "date_Of_birth",
            "phone",
            "joining_date",
            "qualification",
            "experience",
            "teacher_information",
        ]


class TeacherPostSerializer(serializers.ModelSerializer):
    teacher_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    school_teacher = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Teacher
        fields = [
            "uid",
            "school_teacher",
            "teacher_user",
            "name",
            "gender",
            "date_Of_birth",
            "phone",
            "joining_date",
            "qualification",
            "experience",
            "slug",
            "image",
        ]

    def create(self, validated_data):
        image = validated_data.pop("image", None)
        teacher = super().create(validated_data)
        if image:
            TeacherImage.objects.create(teacher_info=teacher, image=image)
        return teacher
