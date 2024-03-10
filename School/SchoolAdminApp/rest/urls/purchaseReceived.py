from django.urls import path

from SchoolAdminApp.rest.views.purchaseReceived import (
    PurchaseReceivedListCreateView,
    PurchaseReceivedRetrieveUpdateDeleteView,
)


urlpatterns = [
    path(
        "<slug:school_slug>/",
        PurchaseReceivedListCreateView.as_view(),
        name="purchase_received_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        PurchaseReceivedRetrieveUpdateDeleteView.as_view(),
        name="purchase_received_delete",
    ),
]
