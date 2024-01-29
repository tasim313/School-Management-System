from rest_framework import serializers

from common.models import SchoolInformationOnBoarding
from core.models import ClassAttendance, User, SchoolClass, SchoolSection
from StudentApp.models import Student


from core.rest.serializers.schoolClass import SchoolClassListSerializer
from core.rest.serializers.SchoolSection import SchoolSectionSerializer

from StudentApp.rest.serializers.student import StudentInformationListSerializer
from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)


class UserSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "role",
            "firstName",
            "lastName",
        ]


class ClassAttendanceListSerializer(serializers.ModelSerializer):
    attendance_class = SchoolClassListSerializer()
    attendance_section = SchoolSectionSerializer()
    attendance_student = StudentInformationListSerializer()
    school = SchoolInformationOnBoardingListSerializer()
    marked_by = UserSlimSerializer()

    class Meta:
        model = ClassAttendance
        fields = [
            "uid",
            "attendance_class",
            "attendance_section",
            "attendance_student",
            "school",
            "marked_by",
            "is_present",
            "on_leave",
            "date",
            "late_arrival",
            "early_departure",
            "leave_reason",
            "attendance_type",
            "comments",
        ]


class ClassAttendancePostSerializer(serializers.ModelSerializer):
    attendance_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(), slug_field="uid"
    )
    attendance_section = serializers.SlugRelatedField(
        queryset=SchoolSection.objects.all(), slug_field="uid"
    )
    attendance_student = serializers.SlugRelatedField(
        queryset=Student.objects.all(), slug_field="uid"
    )
    school = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(), slug_field="uid"
    )

    class Meta:
        model = ClassAttendance
        fields = [
            "uid",
            "attendance_class",
            "attendance_section",
            "attendance_student",
            "school",
            "marked_by",
            "is_present",
            "on_leave",
            "date",
            "late_arrival",
            "early_departure",
            "leave_reason",
            "attendance_type",
            "comments",
        ]
