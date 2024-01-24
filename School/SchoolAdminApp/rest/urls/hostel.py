"""Urls for Hostel REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.hostel import (
    HostelListCreateView,
    HostelRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        HostelListCreateView.as_view(),
        name="hostel_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        HostelRetrieveUpdateDeleteView.as_view(),
        name="hostel_retrieve_update_delete",
    ),
]
