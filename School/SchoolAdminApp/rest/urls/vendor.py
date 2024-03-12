from django.urls import path

from SchoolAdminApp.rest.views.vendor import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        VendorListCreateView.as_view(),
        name="vendor_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        VendorRetrieveUpdateDeleteView.as_view(),
        name="vendor_retrieve_update_delete"
    )
]
