from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import FeesCategory
from SchoolAdminApp.rest.serializers.feesCategory import FeesCategoryListSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class FeesCategoryListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeesCategoryListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = FeesCategory.objects.filter(
            status=Status.Active,
            school_fees__slug=school_slug,
        ).select_related(
            "school_fees"
        )

        return queryset


class FeesCategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeesCategoryListSerializer
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

        fees_category = FeesCategory.objects.filter(
            status=Status.Active,
            school_fees__slug=school_slug,
        ).select_related(
            "school_fees"
        )

        return fees_category
