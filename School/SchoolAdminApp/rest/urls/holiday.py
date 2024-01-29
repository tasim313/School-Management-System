from django.urls import path

from SchoolAdminApp.rest.views.holiday import (
    HolidayManagementListCreateView,
    HolidayManagementRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        HolidayManagementListCreateView.as_view(),
        name="holiday_list_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        HolidayManagementRetrieveUpdateDeleteView.as_view(),
        name="holiday_retrieve_update_delete"
    )
]
