from django.urls import path

from StudentApp.rest.views.student_current_status import StudentCurrentStatusListCreateView, StudentCurrentStatusRetrieveUpdateDeleteView


urlpatterns = [
    path(
        "<slug:school_slug>/",
        StudentCurrentStatusListCreateView.as_view(),
        name="student-status-list",
    ),
    path(
        "<slug:slug>/<uuid:uid>/",
        StudentCurrentStatusRetrieveUpdateDeleteView.as_view(),
        name="student-status-details",
    ),
]
