"""URLs for the Sports Information REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.sports_information import (
    SportsInformationListCreateView,
    SportsInformationRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        SportsInformationListCreateView.as_view(),
        name="sports_information_list_create",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SportsInformationRetrieveUpdateDeleteView.as_view(),
        name="sports_information_retrieve_update_delete",
    ),
]
