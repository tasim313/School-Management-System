"""Urls for Transport REST API"""

from django.urls import path
from SchoolAdminApp.rest.views.transport import (
    TransportListCreateView,
    TransportRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        TransportListCreateView.as_view(),
        name="transport_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        TransportRetrieveUpdateDeleteView.as_view(),
        name="transport_retrieve_update_delete"
    )
]
