from django.urls import path
from SchoolAdminApp.rest.views.library import LibraryListCreateView, LibraryRetrieveUpdateDeleteView

urlpatterns = [
    path(
        "",
        LibraryListCreateView.as_view(),
        name="library_list_create"
    ),
    path(
        "<slug:slug>/",
        LibraryRetrieveUpdateDeleteView.as_view(),
        name="library_retrieve_update_delete"
    )
]
