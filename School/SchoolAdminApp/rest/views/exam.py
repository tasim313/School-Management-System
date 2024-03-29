"""Views for Exam model."""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import Exam
from SchoolAdminApp.rest.serializers.exam import ExamListSerializer, ExamListDetailSerializer

from common.choice import Status
from common.pagination import StandardResultsSetPagination


class ExamListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ExamListSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        # Don't allow non-authenticated user to create via POST
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return [
                AllowAny()
            ]
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ExamListDetailSerializer
        return ExamListSerializer
    

    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        queryset = Exam.objects.filter(
            status=Status.Active,
            school_exam__slug=school_slug,
        ).select_related(
            "school_exam",
            "exam_class",
            "exam_section",
            "exam_subject",
        )

        return queryset


class ExamRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExamListSerializer
    lookup_field = "uid"

    def get_permissions(self):
        # Don't allow non-authenticated user request via PUT, PATCH, DELETE
        if (
                self.request.method == "PUT" or
                self.request.method == "PATCH" or
                self.request.method == "DELETE"
        ):
            return [IsAuthenticated()]
        else:
            return [AllowAny()]


    def get_queryset(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        return Exam.objects.filter(
            status=Status.Active,
            school_exam__slug=school_slug,
        ).select_related(
            "school_exam",
            "exam_class",
            "exam_section",
            "exam_subject",
        )
