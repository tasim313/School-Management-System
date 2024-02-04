"""Urls for Semester REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.semester import (
    SemesterListCreate,
    SemesterRetrieveUpdateDelete
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        SemesterListCreate.as_view(),
        name="semester_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SemesterRetrieveUpdateDelete.as_view(),
        name="semester_retrieve_update_delete"
    ),
]
