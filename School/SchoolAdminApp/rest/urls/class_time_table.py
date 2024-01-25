"""URLs for the SchoolAdminApp REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.class_time_table import (
    ClassTimeTableListCreateView,
    ClassTimeTableRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        ClassTimeTableListCreateView.as_view(),
        name="class_time_table_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        ClassTimeTableRetrieveUpdateDeleteView.as_view(),
        name="class_time_table_retrieve_update_delete",
    ),
]
