from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Subject
from SchoolAdminApp.rest.serializers.subject import SubjectListSerializer

from common.choice import Status


class SubjectListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Subject.objects.filter(
            status=Status.Active,
            school_subject__slug=school_slug,
        ).select_related("school_subject", "class_subject")

        return queryset


class SubjectRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectListSerializer
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

        subject = Subject.objects.filter(
            status=Status.Active,
            school_subject__slug=school_slug,
        ).select_related("school_subject", "class_subject")

        return subject
