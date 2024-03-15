from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.choice import Status
from common.pagination import StandardResultsSetPagination

from core.models import SchoolSection
from core.rest.serializers.SchoolSection import SchoolSectionSerializer


class SchoolSectionListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolSectionSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = SchoolSection.objects.filter(
            status=Status.Active,
            school_class__school_info__slug=school_slug,
        ).select_related("school_class")

        return queryset


class SchoolSectionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SchoolSectionSerializer
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

        section = SchoolSection.objects.filter(
            status=Status.Active,
            school_class__school_info__slug=school_slug,
        ).select_related("school_class")

        return section
