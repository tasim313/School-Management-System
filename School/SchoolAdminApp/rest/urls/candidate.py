from django.urls import path

from SchoolAdminApp.rest.views.candidate import (
    EmployeeCandidateListCreateView,
    EmployeeCandidateRetrieveUpdateDeleteView,
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        EmployeeCandidateListCreateView.as_view(),
        name="candidate_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        EmployeeCandidateRetrieveUpdateDeleteView.as_view(),
        name="candidate_delete",
    ),
]
