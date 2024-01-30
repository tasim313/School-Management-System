from django.urls import path

from SchoolAdminApp.rest.views.feesInformation import (
    FeesInformationListCreateView,
    FeesInformationRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        FeesInformationListCreateView.as_view(),
        name="fees_information_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        FeesInformationRetrieveUpdateDeleteView.as_view(),
        name="fees_information_delete",
    ),
]
