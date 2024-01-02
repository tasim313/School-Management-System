from django.urls import path

from core.rest.views.about import (
    SchoolWebsiteAboutInformationAPIView,
    SchoolWebsiteAboutInformationListView,
    SchoolWebsiteAboutFileAPIView,
    SchoolWebsiteAboutImageListView
)


urlpatterns = [
    path(
        "",
        SchoolWebsiteAboutInformationAPIView.as_view(),
        name="school-website-about-information-create",
    ),
    path(
        "<slug:school_slug>/",
        SchoolWebsiteAboutInformationListView.as_view(),
        name="school-website-about-list",
    ),
    path(
        "image/create/", 
        SchoolWebsiteAboutFileAPIView.as_view(),
        name="school-website-about-image-create",
    ),
    path(
        "image/<slug:school_slug>/",
        SchoolWebsiteAboutImageListView.as_view(),
        name="school-website-about-image-list",
    ),
]
