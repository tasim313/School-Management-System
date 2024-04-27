"""Views for School Result model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from SchoolAdminApp.models import SchoolResult
from SchoolAdminApp.rest.serializers.school_result import (
    SchoolResultListSerializer,
)
from common.custom_permission import IsStudent, IsTeacher, IsSchoolAdmin


class SchoolResultListView(generics.ListAPIView):
    permission_classes = [IsAdminUser | IsTeacher | IsSchoolAdmin]
    serializer_class = SchoolResultListSerializer

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = SchoolResult.objects.filter(
            school__slug=school_slug,
        ).select_related(
            "school",
            "school_class",
            "school_section",
            "school_semester",
            "school_student",
        ).prefetch_related(
            "passed_subjects_result",
            "failed_subjects_result__result_subject",
            "failed_subjects_result",
            "failed_subjects_result__result_subject",
        )

        return queryset


class SchoolResultRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser | IsTeacher | IsSchoolAdmin]
    serializer_class = SchoolResultListSerializer
    lookup_field = "uid"

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = SchoolResult.objects.filter(
            school__slug=school_slug,
        ).select_related(
            "school",
            "school_class",
            "school_section",
            "school_semester",
            "school_student",
        ).prefetch_related(
            "passed_subjects_result",
            "failed_subjects_result__result_subject",
            "failed_subjects_result",
            "failed_subjects_result__result_subject",
        )

        return queryset


class StudentSchoolResultListView(generics.ListAPIView):
    permission_classes = [IsStudent]
    serializer_class = SchoolResultListSerializer

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)
        user_id = self.request.user.id

        queryset = SchoolResult.objects.filter(
            school__slug=school_slug,
            school_student__user_id=user_id,
        ).select_related(
            "school",
            "school_class",
            "school_section",
            "school_semester",
            "school_student",
        ).prefetch_related(
            "passed_subjects_result",
            "failed_subjects_result__result_subject",
            "failed_subjects_result",
            "failed_subjects_result__result_subject",
        )

        return queryset


class StudentSchoolResultRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsStudent]
    serializer_class = SchoolResultListSerializer
    lookup_field = "uid"

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)
        user_id = self.request.user.id

        queryset = SchoolResult.objects.filter(
            school__slug=school_slug,
            school_student__user_id=user_id,
        ).select_related(
            "school",
            "school_class",
            "school_section",
            "school_semester",
            "school_student",
        ).prefetch_related(
            "passed_subjects_result",
            "failed_subjects_result__result_subject",
            "failed_subjects_result",
            "failed_subjects_result__result_subject",
        )

        return queryset
