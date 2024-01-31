from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.models import (
    WebsiteTeacherInformation, 
    WebsiteManagingCommitteeMemberInformation, 
    WebsiteStaffInformation, 
    WebSiteFacultyInformation
    )
from core.rest.serializers.team import (
    WebsiteTeacherInformationListSerializer, 
    WebsiteManagingCommitteeMemberInformationListSerializer,
    WebsiteStaffInformationListSerializer,
    WebSiteFacultyInformationListSerializer,
    )

from common.choice import Status


class WebsiteTeacherInformationListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteTeacherInformationListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteTeacherInformation.objects.filter(
            status=Status.Active,
            school_teacher__slug=school_slug,
        ).select_related(
            "school_teacher"
        )

        return queryset


class WebsiteTeacherInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteTeacherInformationListSerializer
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

        school_teacher = WebsiteTeacherInformation.objects.filter(
            status=Status.Active,
            school_teacher__slug=school_slug,
        ).select_related(
            "school_teacher"
        )

        return school_teacher



class WebsiteManagingCommitteeMemberInformationListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteManagingCommitteeMemberInformationListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteManagingCommitteeMemberInformation.objects.filter(
            status=Status.Active,
            school_managing_committee_member__slug=school_slug,
        ).select_related(
            "school_managing_committee_member"
        )

        return queryset


class WebsiteManagingCommitteeMemberInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteManagingCommitteeMemberInformationListSerializer
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

        school_managing_committee_member = WebsiteManagingCommitteeMemberInformation.objects.filter(
            status=Status.Active,
            school_managing_committee_member__slug=school_slug,
        ).select_related(
            "school_managing_committee_member"
        )

        return school_managing_committee_member




class WebsiteStaffInformationListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteStaffInformationListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteStaffInformation.objects.filter(
            status=Status.Active,
            school_staff__slug=school_slug,
        ).select_related(
            "school_staff"
        )

        return queryset


class WebsiteStaffInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebsiteStaffInformationListSerializer
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

        school_staff = WebsiteStaffInformation.objects.filter(
            status=Status.Active,
            school_staff__slug=school_slug,
        ).select_related(
            "school_staff",
        )

        return school_staff



class WebSiteFacultyInformationListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WebSiteFacultyInformationListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebSiteFacultyInformation.objects.filter(
            status=Status.Active,
            school_faculty__slug=school_slug,
        ).prefetch_related(
            "school_faculty",
            "teachers",
            "staff_members",
            "managing_committee_member"
        )

        return queryset


class WebSiteFacultyInformationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WebSiteFacultyInformationListSerializer
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

        school_faculty = WebSiteFacultyInformation.objects.filter(
            status=Status.Active,
            school_faculty__slug=school_slug,
        ).prefetch_related(
            "school_faculty",
            "teachers",
            "staff_members",
            "managing_committee_member"
        )

        return school_faculty
