"""Views for GradingConfig model."""

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from SchoolAdminApp.models import GradingConfig
from SchoolAdminApp.rest.serializers.grading_config import GradingConfigListSerializer

from common.choice import Status


class GradingConfigListCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GradingConfigListSerializer


class GradingConfigRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GradingConfigListSerializer

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

    def get_object(self):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        # get grading config object or 404
        grading_config = get_object_or_404(
            GradingConfig.objects.filter(
                status=Status.Active,
                school_grading__slug=school_slug,
            ).select_related("school_grading")
        )

        return grading_config


class SchoolGradingConfigDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Get school_slug from URL
        school_slug = self.kwargs.get("school_slug", None)

        # get grading config object or 404
        grading_config = get_object_or_404(
            GradingConfig.objects.filter(
                status=Status.Active,
                school_grading__slug=school_slug,
            ).select_related("school_grading")
        )

        # customize response object to send
        make_response = {
            "uid": grading_config.uid,
            "slug": grading_config.slug,
            "school_grading": grading_config.school_grading.uid,
            "letter_grade_A_plus": f"{grading_config.letter_grade_A_plus} - 100",
            "letter_grade_A": f"{grading_config.letter_grade_A} - {grading_config.letter_grade_A_plus - 1}",
            "letter_grade_A_minus": f"{grading_config.letter_grade_A_minus} - {grading_config.letter_grade_A - 1}",
            "letter_grade_B": f"{grading_config.letter_grade_B} - {grading_config.letter_grade_A_minus - 1}",
            "letter_grade_C": f"{grading_config.letter_grade_C} - {grading_config.letter_grade_B - 1}",
            "letter_grade_D": f"{grading_config.letter_grade_D} - {grading_config.letter_grade_C - 1}",
            "letter_grade_F": f"0 - {grading_config.letter_grade_F}",
        }

        return Response(make_response, status=status.HTTP_200_OK)
