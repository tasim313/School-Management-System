from django.urls import path
from core.rest.views.websiteInfo import (
    SchoolWebsiteAPIView,
    WebsiteInformationListView,
    SchoolWebsiteUpdateAPIView,
    WebsiteGalleryInfoList,
    WebsiteGalleryInfoDetail,
)

urlpatterns = [
    path(
        "",
        SchoolWebsiteAPIView.as_view(),
        name="school-website-information-create",
    ),
    path(
        "gallery/",
        WebsiteGalleryInfoList.as_view(),
        name="school-gallery",
    ),
    path(
        "<slug:school_slug>/",
        WebsiteInformationListView.as_view(),
        name="school_website_information",
    ),
    path(
        "update/<uuid:uid>/",
        SchoolWebsiteUpdateAPIView.as_view(),
        name="school-website-update",
    ),
    path(
        "gallery/<uuid:uid>/",
        WebsiteGalleryInfoDetail.as_view(),
        name="school-gallery-detail",
    ),
]
