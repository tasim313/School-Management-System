from django.urls import path
from core.rest.views.websiteInfo import (
    SchoolWebsiteAPIView,
    WebsiteInformationListView,
    SchoolWebsiteUpdateAPIView,
    WebsiteGalleryInfoCreate,
    WebsiteGalleryUpdateAPIView,
    WebsiteGalleryInfoListView,
    WebsiteGalleryInfoListDestroyView
)

urlpatterns = [
    path(
        "",
        SchoolWebsiteAPIView.as_view(),
        name="school-website-information-create",
    ),
    path(
        "gallery/",
        WebsiteGalleryInfoCreate.as_view(),
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
        WebsiteGalleryUpdateAPIView.as_view(),
        name="school-gallery-update",
    ),
    path(
        "gallery/<slug:school_slug>/",
        WebsiteGalleryInfoListView.as_view(),
        name="school-gallery-list",
    ),
    path(
        "gallery/<slug:school_slug>/<uuid:uid>/",
        WebsiteGalleryInfoListDestroyView.as_view(),
        name="school-gallery-delete",
    ),
]
