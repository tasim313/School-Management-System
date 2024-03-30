from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import FeesInformation
from SchoolAdminApp.rest.serializers.feesInformation import (
    FeesInformationSerializer,
    FeesInformationDetailSerializer
)

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class FeesInformationListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeesInformationSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FeesInformationDetailSerializer
        return FeesInformationSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = FeesInformation.objects.filter(
            status=Status.Active,
            fees_category__school_fees__slug=school_slug,
        ).select_related(
            "fees_category",
            "fess_class",
            "fess_section"
        )

        return queryset


class FeesInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeesInformationSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return []

    def get_serializer_class(self):
        if self.request.method == "GET":
            return FeesInformationDetailSerializer
        return FeesInformationSerializer

    def get_queryset(self):

        school_slug = self.kwargs.get("school_slug", None)

        fees_information = FeesInformation.objects.filter(
            status=Status.Active,
            fees_category__school_fees__slug=school_slug,
        ).select_related(
            "fees_category",
            "fess_class",
            "fess_section"
        )

        return fees_information
