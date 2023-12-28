from django.urls import path

from core.rest.views.about import (
    SchoolWebsiteAboutInformationAPIView,
    SchoolWebsiteAboutInformationListView
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
    )
]
