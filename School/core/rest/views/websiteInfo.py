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
    SchoolContactInformation
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
                'message': 'School Website Information Create successful.',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        except serializers.ValidationError as e:
            error_data = {
                'message': 'School Website Information failed.',
                'errors': e.detail
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)
        
        

class WebsiteInformationListView(generics.ListAPIView):
    queryset = WebsiteInformation.objects.all()
    serializer_class = websiteInfo.WebsiteInformationSerializer

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        return self.queryset.filter(school_website__slug=school_slug)

    