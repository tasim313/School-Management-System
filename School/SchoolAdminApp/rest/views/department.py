from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Department
from SchoolAdminApp.rest.serializers.department import DepartmentListSerializer

from common.choice import Status


class DepartmentListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmentListSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Department.objects.filter(
            status=Status.Active,
            school_department__slug=school_slug,
        ).select_related("school_department")

        return queryset


class DepartmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = DepartmentListSerializer
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

        library = Department.objects.filter(
            status=Status.Active,
            school_department__slug=school_slug,
        ).select_related("school_department")

        return library
