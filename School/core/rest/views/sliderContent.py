from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework import status, serializers


from ..serializers import sliderContent

from ...models import (
    WebsiteHomeSliderContent
)

import logging

logger = logging.getLogger(__name__)


class WebsiteHomeSliderContentAPIView(generics.CreateAPIView):
    serializer_class = sliderContent.CreateWebsiteHomeSliderContentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            response_data = {
                'message': 'Website HomeSlider Content Create successful.',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        except serializers.ValidationError as e:
            error_data = {
                'message': 'Website HomeSlider Content failed.',
                'errors': e.detail
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)