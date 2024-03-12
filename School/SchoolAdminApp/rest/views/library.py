"""Views for Library model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Library
from SchoolAdminApp.rest.serializers.library import (
    LibraryListSerializer,
    LibraryPostSerializer,
)

from common.choice import Status


class LibraryListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LibraryListSerializer

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Library.objects.filter(
            status=Status.Active,
            school_library__slug=school_slug,
        ).select_related(
            "school_library",
            "library_department",
            "library_class",
        )

        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "POST":
            return LibraryPostSerializer
        return super().get_serializer(*args, **kwargs)


class LibraryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LibraryListSerializer
    lookup_field = "uid"

    def get_permissions(self):
        # Don't allow non-authenticated user request via PUT, PATCH, DELETE
        if (
            self.request.method == "PUT"
            or self.request.method == "PATCH"
            or self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        library = Library.objects.filter(
            status=Status.Active,
            school_library__slug=school_slug,
        ).select_related(
            "school_library",
            "library_department",
            "library_class",
        )

        return library
