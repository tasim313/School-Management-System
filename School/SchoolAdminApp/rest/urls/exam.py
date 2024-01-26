"""URLs for the Exam REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.exam import (
    ExamListCreateView,
    ExamRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        ExamListCreateView.as_view(),
        name="exam_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        ExamRetrieveUpdateDeleteView.as_view(),
        name="exam_retrieve_update_delete",
    ),
]
