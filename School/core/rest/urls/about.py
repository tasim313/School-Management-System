from django.urls import path

from core.rest.views.about import (
    SchoolWebsiteAboutInformationAPIViewListCreateView,
    SchoolWebsiteAboutInformationRetrieveUpdateDeleteView,
    WebsiteAboutFileListCreateView,
    WebsiteAboutFileRetrieveUpdateDeleteView,
    WebsiteFunFactContentListCreateView,
    WebsiteFunFactContentRetrieveUpdateDeleteView,
    WebsiteAboutWinningAwardsListCreateView,
    WebsiteAboutWinningAwardsRetrieveUpdateDeleteView,
    AboutListView
)


urlpatterns = [
    path(
        "<slug:school_slug>/",
        SchoolWebsiteAboutInformationAPIViewListCreateView.as_view(),
        name="school-website-about-information-create",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SchoolWebsiteAboutInformationRetrieveUpdateDeleteView.as_view(),
        name="school-website-about-update-delete",
    ),
    path(
        "<slug:school_slug>/file/", 
        WebsiteAboutFileListCreateView.as_view(),
        name="school-website-about-file-create",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/file/",
        WebsiteAboutFileRetrieveUpdateDeleteView.as_view(),
        name="school-website-about-file-delete",
    ),
    path(
        "<slug:school_slug>/content/", 
        WebsiteFunFactContentListCreateView.as_view(),
        name="school-website-about-content-create",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/content/",
        WebsiteFunFactContentRetrieveUpdateDeleteView.as_view(),
        name="school-website-about-content-delete",
    ),
    path(
        "<slug:school_slug>/award/", 
        WebsiteAboutWinningAwardsListCreateView.as_view(),
        name="school-website-about-award-create",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/award/",
        WebsiteAboutWinningAwardsRetrieveUpdateDeleteView.as_view(),
        name="school-website-about-award-delete",
    ),
    path(
        "<slug:school_slug>/list/",
        AboutListView.as_view(),
        name="about-list"
    ),
   
]
