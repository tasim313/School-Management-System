from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, serializers
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404

from ..serializers import websiteInfo

from ...models import (
    WebsiteInformation,
    SchoolAddressInformation,
    SchoolContactInformation,
    WebSiteGalleryInformation,
)

import logging

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


class WebsiteInformationListView(generics.ListAPIView):
    queryset = WebsiteInformation.objects.all()
    serializer_class = websiteInfo.WebsiteInformationSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school_website__slug=school_slug)


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


class WebsiteGalleryInfoList(generics.ListCreateAPIView):
    queryset = WebSiteGalleryInformation.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return websiteInfo.WebsiteGalleryInfoPostSerializer
        return websiteInfo.WebsiteGalleryInfoListSerializer


class WebsiteGalleryInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebSiteGalleryInformation.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "POST":
            return websiteInfo.WebsiteGalleryInfoPostSerializer
        return websiteInfo.WebsiteGalleryInfoListSerializer
