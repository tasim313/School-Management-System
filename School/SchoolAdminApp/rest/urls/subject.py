from django.urls import path

from SchoolAdminApp.rest.views.subject import (
    SubjectListCreateView,
    SubjectRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        SubjectListCreateView.as_view(),
        name="subject_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SubjectRetrieveUpdateDeleteView.as_view(),
        name="subject_retrieve_update_delete"
    )
]