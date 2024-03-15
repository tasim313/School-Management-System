from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import StandardResultsSetPagination

from core.models import Testimonials
from core.rest.serializers.testimonial import (
    TestimonialsCreateSerializer,
    TestimonialsUpdateSerializer,
    TestimonialsListSerializer
)


class TestimonialsAPIView(generics.CreateAPIView):
    serializer_class = TestimonialsCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                "message": "Testimonials Create successful.",
                "data": serializer.data,
            }
            return Response(
                response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except serializers.ValidationError as e:
            error_data = {
                "message": "Testimonials failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class TestimonialsListView(generics.ListAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school_testimonials__slug=school_slug)


class TestimonialsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TestimonialsUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"
    allowed_methods = [
        "PUT",
        "PATCH",
    ]

    def get_queryset(self):
        return Testimonials.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                "message": "Testimonials update successful.",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            error_data = {
                "message": "Testimonials update failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(user_updated=self.request.user)


class TestimonialsDestroy(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsListSerializer
    lookup_field = "uid"

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school_testimonials__slug=school_slug)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
