from django.urls import path

from SchoolAdminApp.rest.views.purchasesRequest import (
    PurchaseRequestListCreateView,
    PurchaseRequestRetrieveUpdateDeleteView,
)


urlpatterns = [
    path(
        "<slug:school_slug>/",
        PurchaseRequestListCreateView.as_view(),
        name="purchase_request_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        PurchaseRequestRetrieveUpdateDeleteView.as_view(),
        name="purchase_request_delete",
    ),
]