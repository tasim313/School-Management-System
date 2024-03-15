from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import EmployeeCandidate
from SchoolAdminApp.rest.serializers.candidate import EmployeeCandidateSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class EmployeeCandidateListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeCandidateSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = EmployeeCandidate.objects.filter(
            status=Status.Active,
            school_candidate__slug=school_slug,
        ).select_related(
            "school_candidate",
            "job_category"
        )

        return queryset


class EmployeeCandidateRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeCandidateSerializer
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

        candidate = EmployeeCandidate.objects.filter(
            status=Status.Active,
            school_candidate__slug=school_slug,
        ).select_related(
            "school_candidate",
            "job_category"
        )

        return candidate
