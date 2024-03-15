from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Vendor
from SchoolAdminApp.rest.serializers.vendor import VendorListSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class VendorListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VendorListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Vendor.objects.filter(
            status=Status.Active,
            school_vendor__slug=school_slug,
        ).select_related(
            "school_vendor"
        )

        return queryset


class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VendorListSerializer
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

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        vendor = Vendor.objects.filter(
            status=Status.Active,
            school_vendor__slug=school_slug,
        ).select_related(
            "school_vendor"
        )

        return vendor
