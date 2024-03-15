import logging

from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import StandardResultsSetPagination

from ..serializers import sliderContent

from ...models import (
    WebsiteHomeSliderContent
)

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


class SliderContentListView(generics.ListAPIView):
    serializer_class = sliderContent.SliderContentListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)

        queryset = WebsiteHomeSliderContent.objects.filter(
            website_home_slider_content__slug=school_slug,
            status="Active",
        ).select_related('website_home_slider_content')

        return queryset


class WebsiteHomeSliderContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = sliderContent.UpdateWebsiteHomeSliderContentSerializer
    lookup_field = 'uid'

    def get_queryset(self):
        school_slug = self.kwargs.get("school_slug", None)
        queryset = WebsiteHomeSliderContent.objects.filter(
            website_home_slider_content__slug=school_slug
        ).select_related('website_home_slider_content')

        return queryset
