"""URLs for the GradingConfig REST API."""

from django.urls import path

from SchoolAdminApp.rest.views.grading_config import (
    GradingConfigListCreateView,
    GradingConfigRetrieveUpdateDeleteView,
    SchoolGradingConfigDetail,
)

urlpatterns = [
    path(
        "",
        GradingConfigListCreateView.as_view(),
        name="grading_config_list_create"
    ),
    path(
        "<slug:school_slug>/",
        GradingConfigRetrieveUpdateDeleteView.as_view(),
        name="grading_config_retrieve_update_delete",
    ),
    path(
        "detail/<slug:school_slug>/",
        SchoolGradingConfigDetail.as_view(),
        name="school_grading_config_detail",
    ),
]
