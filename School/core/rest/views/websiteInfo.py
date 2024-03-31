import logging

from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import StandardResultsSetPagination

from ..serializers import websiteInfo

from ...models import (
    WebsiteInformation,
    WebSiteGalleryInformation,
)

logger = logging.getLogger(__name__)


class SchoolWebsiteAPIView(generics.CreateAPIView):
    serializer_class = websiteInfo.SchoolWebsiteCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                "message": "School Website Information Create successful.",
                "data": serializer.data,
            }
            return Response(
                response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except serializers.ValidationError as e:
            error_data = {
                "message": "School Website Information failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class WebsiteInformationListView(APIView):
    serializer_class = websiteInfo.WebsiteInformationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        school_slug = self.kwargs.get("school_slug", None)

        try:
            website_info = WebsiteInformation.objects.select_related(
                "school_website",
                "school_address",
                "school_contact",
            ).get(school_website__slug=school_slug)
        except WebsiteInformation.DoesNotExist:
            return Response(
                {"message": "School Website Information not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(website_info)
        return Response(serializer.data)


class SchoolWebsiteUpdateAPIView(generics.UpdateAPIView):
    serializer_class = websiteInfo.SchoolWebsiteUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"
    allowed_methods = [
        "PUT",
        "PATCH",
    ]

    def get_queryset(self):
        return WebsiteInformation.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                "message": "School Website Information update successful.",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            error_data = {
                "message": "School Website Information update failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(user_updated=self.request.user)


class WebsiteGalleryInfoCreate(generics.CreateAPIView):
    serializer_class = websiteInfo.SchoolWebsiteGallerySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                "message": "Gallery Image Create successful.",
                "data": serializer.data,
            }
            return Response(
                response_data, status=status.HTTP_201_CREATED, headers=headers
            )
        except serializers.ValidationError as e:
            error_data = {
                "message": "Gallery Image failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class WebsiteGalleryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = websiteInfo.SchoolWebsiteGalleryUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"
    allowed_methods = [
        "PUT",
        "PATCH",
    ]

    def get_queryset(self):
        return WebSiteGalleryInformation.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            response_data = {
                "message": "Gallery Image update successful.",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            error_data = {
                "message": "Gallery Image update failed.",
                "errors": e.detail,
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(user_updated=self.request.user)


class WebsiteGalleryInfoListView(generics.ListAPIView):
    queryset = WebSiteGalleryInformation.objects.all()
    serializer_class = websiteInfo.WebsiteGalleryInfoListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school_website_gallery__slug=school_slug)



class WebsiteGalleryInfoListDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = websiteInfo.WebsiteGalleryInfoListSerializer
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
        gallery = WebSiteGalleryInformation.objects.filter(
            school_website_gallery__slug=school_slug
        ).select_related(
            "school_website_gallery"
        )

        return gallery