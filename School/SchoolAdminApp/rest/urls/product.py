from django.urls import path

from SchoolAdminApp.rest.views.product import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        ProductListCreateView.as_view(),
        name="product_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        ProductRetrieveUpdateDeleteView.as_view(),
        name="product_retrieve_update_delete"
    )
]
