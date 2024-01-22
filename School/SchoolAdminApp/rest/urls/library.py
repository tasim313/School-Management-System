from django.urls import path

from SchoolAdminApp.rest.views.library import (
    LibraryListCreateView,
    LibraryRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        LibraryListCreateView.as_view(),
        name="library_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        LibraryRetrieveUpdateDeleteView.as_view(),
        name="library_retrieve_update_delete"
    )
]
