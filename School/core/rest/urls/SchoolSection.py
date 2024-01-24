from django.urls import path

from core.rest.views.SchoolSection import (
    SchoolSectionListCreateView,
    SchoolSectionRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        SchoolSectionListCreateView.as_view(),
        name="section_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SchoolSectionRetrieveUpdateDeleteView.as_view(),
        name="section_retrieve_update_delete"
    )
]
