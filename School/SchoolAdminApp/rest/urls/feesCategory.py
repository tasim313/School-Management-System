from django.urls import path

from SchoolAdminApp.rest.views.feesCategory import (
    FeesCategoryListCreateView,
    FeesCategoryRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        FeesCategoryListCreateView.as_view(),
        name="fees_category_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        FeesCategoryRetrieveUpdateDeleteView.as_view(),
        name="fees_category_retrieve_update_delete"
    )
]
