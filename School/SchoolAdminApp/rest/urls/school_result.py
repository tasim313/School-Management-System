"""URLs for the school result API."""

from django.urls import path

from SchoolAdminApp.rest.views.school_result import (
    SchoolResultListView,
    SchoolResultRetrieveView
)


urlpatterns = [
    path(
        "<slug:school_slug>/",
        SchoolResultListView.as_view(),
        name="school_result_list",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SchoolResultRetrieveView.as_view(),
        name="school_result_retrieve",
    ),
]
