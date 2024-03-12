from django.urls import path

from SchoolAdminApp.rest.views.category import (
    ProductCategoryListCreateView,
    ProductCategoryRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        ProductCategoryListCreateView.as_view(),
        name="product_category_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        ProductCategoryRetrieveUpdateDeleteView.as_view(),
        name="product_category_retrieve_update_delete"
    )
]
