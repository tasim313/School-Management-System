from django.urls import path
from core.rest.views.sliderContent import (
    WebsiteHomeSliderContentAPIView,
    SliderContentListView
)


urlpatterns = [
    path('', 
         WebsiteHomeSliderContentAPIView.as_view(),
         name='website-homeSlider-content-create'),
    path(
        "<slug:school_slug>/",
        SliderContentListView.as_view(),
        name="school_website_information",
    ),
]