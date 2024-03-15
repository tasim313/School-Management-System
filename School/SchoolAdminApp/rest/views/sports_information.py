"""Views for Sports Information model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import SportsInformation
from SchoolAdminApp.rest.serializers.sports_information import SportsInformationListSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class SportsInformationListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SportsInformationListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = SportsInformation.objects.filter(
            status=Status.Active,
            school_sports__slug=school_slug,
        ).select_related("school_sports")

        return queryset


class SportsInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SportsInformationListSerializer
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

        sports_information = SportsInformation.objects.filter(
            status=Status.Active,
            school_sports__slug=school_slug,
        ).select_related("school_sports")

        return sports_information
