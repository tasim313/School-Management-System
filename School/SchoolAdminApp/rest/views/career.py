from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Career
from SchoolAdminApp.rest.serializers.career import CareerListSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class CareerListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CareerListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Career.objects.filter(
            status=Status.Active,
            school_career__slug=school_slug,
        ).select_related(
            "school_career",
            "career_department"
        )

        return queryset


class CareerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CareerListSerializer
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

        career = Career.objects.filter(
            status=Status.Active,
            school_career__slug=school_slug,
        ).select_related(
            "school_career",
            "career_department"
        )

        return career
