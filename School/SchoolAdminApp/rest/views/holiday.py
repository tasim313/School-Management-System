from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import HolidayManagement
from SchoolAdminApp.rest.serializers.holiday import HolidayManagementListSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class HolidayManagementListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HolidayManagementListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = HolidayManagement.objects.filter(
            status=Status.Active,
            school_holiday__slug=school_slug,
        ).select_related(
            "school_holiday"
        )

        return queryset


class HolidayManagementRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HolidayManagementListSerializer
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

        holiday = HolidayManagement.objects.filter(
            status=Status.Active,
            school_holiday__slug=school_slug,
        ).select_related(
            "school_holiday"
        )

        return holiday
