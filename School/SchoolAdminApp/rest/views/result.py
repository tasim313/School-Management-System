"""Views for Result model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Result
from SchoolAdminApp.rest.serializers.result import ResultListSerializer

from common.choice import Status

from SchoolAdminApp.filters import ResultFilter
from common.pagination import StandardResultsSetPagination

from common.custom_permission import IsSchoolAdmin, IsStudent, IsTeacher


class ResultListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ResultListSerializer
    filterset_class = ResultFilter
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [
                IsAdminUser() or
                IsTeacher() or
                IsSchoolAdmin(),
            ]
        else:
            return [IsAuthenticated()]

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Result.objects.filter(
            status=Status.Active,
            school_result__slug=school_slug,
        ).select_related(
            "school_result",
            "result_class",
            "result_section",
            "result_semester",
            "result_subject",
            "result_student",
        )

        return queryset


class ResultRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResultListSerializer
    lookup_field = "uid"

    def get_permissions(self):
        # Don't allow non-authenticated user request via PUT, PATCH, DELETE
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [
                IsAdminUser() or
                IsTeacher() or
                IsSchoolAdmin(),
            ]
        else:
            return [IsAuthenticated()]

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        result = Result.objects.filter(
            status=Status.Active,
            school_result__slug=school_slug,
        ).select_related(
            "school_result",
            "result_class",
            "result_section",
            "result_semester",
            "result_subject",
            "result_student",
        )

        return result
