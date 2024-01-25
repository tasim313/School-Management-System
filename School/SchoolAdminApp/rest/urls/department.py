from django.urls import path

from SchoolAdminApp.rest.views.department import (
    DepartmentListCreateView,
    DepartmentRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        DepartmentListCreateView.as_view(),
        name="department_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        DepartmentRetrieveUpdateDeleteView.as_view(),
        name="department_retrieve_update_delete"
    )
]
