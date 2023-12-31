from django.urls import path
from StudentApp.rest.views.student import (
    StudentInformationListView,
    StudentDetail,
)


urlpatterns = [
    path(
        "information/<slug:school_slug>/",
        StudentInformationListView.as_view(),
        name="student-information-list",
    ),
    path(
        "<slug:slug>/",
        StudentDetail.as_view(),
        name="student-details",
    ),
]
