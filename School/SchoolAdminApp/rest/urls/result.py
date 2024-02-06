"""Urls for Result REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.result import (
    ResultListCreateView,
    ResultRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        ResultListCreateView.as_view(),
        name="result_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        ResultRetrieveUpdateDeleteView.as_view(),
        name="result_retrieve_update_delete",
    ),
]
