from django.urls import path

from SchoolAdminApp.rest.views.feesCollection import (
    FeesCollectionListCreateView,
    FeesCollectionRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        FeesCollectionListCreateView.as_view(),
        name="fees_collection_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        FeesCollectionRetrieveUpdateDeleteView.as_view(),
        name="fees_collection_delete",
    ),
]
