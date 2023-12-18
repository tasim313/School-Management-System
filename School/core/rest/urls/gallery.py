from django.urls import path

from core.rest.views.websiteInfo import WebsiteGalleryInfoList

urlpatterns = [
    path(
        "",
        WebsiteGalleryInfoList.as_view(),
        name="school-gallery",
    ),
]
