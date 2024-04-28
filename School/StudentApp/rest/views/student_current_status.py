from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from StudentApp.rest.serializers.student import (
    StudentCurrentStatusListSerializer,
    StudentCurrentStatusDetailsSerializer
)

from StudentApp.models import StudentCurrentStatus

from common.pagination import StandardResultsSetPagination
from StudentApp.filters import StudentCurrentStatusFilter


class StudentCurrentStatusListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentCurrentStatusListSerializer
    pagination_class = StandardResultsSetPagination
    filterset_class = StudentCurrentStatusFilter

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentCurrentStatusDetailsSerializer
        return StudentCurrentStatusListSerializer

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = StudentCurrentStatus.objects.filter(
            student_current_status__school_student__slug=school_slug,
        ).select_related(
            "current_class",
            "current_section",
        )

        return queryset


class StudentCurrentStatusRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentCurrentStatusListSerializer
    lookup_field = "uid"

    def get_permissions(self):
        # Don't allow non-authenticated user request via PUT, PATCH, DELETE
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        current_status = StudentCurrentStatus.objects.filter(
            student_current_status__school_student__slug=school_slug,
        ).select_related(
            "current_class",
            "current_section",
        )

        return current_status
