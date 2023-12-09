from django.urls import path
from core.rest.views.sliderContent import (
    WebsiteHomeSliderContentAPIView
)


urlpatterns = [
    path('', 
         WebsiteHomeSliderContentAPIView.as_view(),
         name='website-homeSlider-content-create'),
]