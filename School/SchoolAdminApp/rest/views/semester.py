"""Views fro Hostel model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Semester
from SchoolAdminApp.rest.serializers.semester import SemesterListSerializer

from common.choice import Status


class SemesterListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SemesterListSerializer

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Semester.objects.filter(
            status=Status.Active,
            school_semester__slug=school_slug,
        ).select_related("school_semester")

        return queryset


class SemesterRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SemesterListSerializer
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

        semester = Semester.objects.filter(
            status=Status.Active,
            school_semester__slug=school_slug,
        ).select_related("school_semester")

        return semester
