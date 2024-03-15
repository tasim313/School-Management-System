from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.choice import Status
from common.pagination import StandardResultsSetPagination

from core.models import AlumniSection, AlumniSectionImage
from core.rest.serializers.alumni import AlumniSectionListSerializer, AlumniSectionImageListSerializer


class AlumniSectionListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AlumniSectionListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = AlumniSection.objects.filter(
            status=Status.Active,
            school_alumni_section__slug=school_slug,
        ).select_related(
            "school_alumni_section"
        )

        return queryset


class AlumniSectionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlumniSectionListSerializer
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

        school_alumni_section = AlumniSection.objects.filter(
            status=Status.Active,
            school_alumni_section__slug=school_slug,
        ).select_related(
            "school_alumni_section"
        )

        return school_alumni_section


class AlumniSectionImageListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AlumniSectionImageListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = AlumniSectionImage.objects.filter(
            status=Status.Active,
            alumni_info__school_alumni_section__slug=school_slug,
        ).select_related(
            "alumni_info"
        )

        return queryset


class AlumniSectionImageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlumniSectionImageListSerializer
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

        alumni_info = AlumniSectionImage.objects.filter(
            status=Status.Active,
            alumni_info__school_alumni_section__slug=school_slug,
        ).select_related(
            "alumni_info"
        )

        return alumni_info
