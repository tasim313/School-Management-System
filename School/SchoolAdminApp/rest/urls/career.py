from django.urls import path

from SchoolAdminApp.rest.views.career import (
    CareerListCreateView,
    CareerRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        CareerListCreateView.as_view(),
        name="career_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        CareerRetrieveUpdateDeleteView.as_view(),
        name="career_delete",
    ),
]
