"""Views for ClassTimeTable model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import ClassTimeTable
from SchoolAdminApp.rest.serializers.class_time_table import ClassTimeTableListSerializer, ClassTimeTableDetailsSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class ClassTimeTableListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ClassTimeTableListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ClassTimeTableDetailsSerializer
        return ClassTimeTableListSerializer

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = ClassTimeTable.objects.filter(
            status=Status.Active,
            school_class_time_table__slug=school_slug,
        ).select_related(
            "school_class_time_table",
            "school_time_table",
            "school_section_time_table",
            "class_time_table_subject",
        )

        return queryset


class ClassTimeTableRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassTimeTableListSerializer
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

        class_time_table = ClassTimeTable.objects.filter(
            status=Status.Active,
            school_class_time_table__slug=school_slug,
        ).select_related(
            "school_class_time_table",
            "school_time_table",
            "school_section_time_table",
            "class_time_table_subject",
        )

        return class_time_table
