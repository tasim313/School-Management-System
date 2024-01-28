from django.urls import path

from core.rest.views.attendance import ClassAttendanceListCreate

urlpatterns = [
    path(
        "",
        ClassAttendanceListCreate.as_view(),
        name="class-attendance-list-create",
    ),
]
