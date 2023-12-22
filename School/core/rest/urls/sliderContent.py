from django.urls import path
from core.rest.views.sliderContent import (
    WebsiteHomeSliderContentAPIView,
    SliderContentListView,
    WebsiteHomeSliderContentDetailView
)


urlpatterns = [
    path('', 
         WebsiteHomeSliderContentAPIView.as_view(),
         name='website-homeSlider-content-create'),
    path(
        "<slug:school_slug>/",
        SliderContentListView.as_view(),
        name="website-homeSlider-content-list",
    ),
    path(
        "<slug:school_slug>/update/<uuid:uid>/",
        WebsiteHomeSliderContentDetailView.as_view(),
        name="website-homeSlider-content-details",
    ),
]