from django.urls import path

from core.rest.views.attendance import ClassAttendanceListCreate, ClassAttendanceDetail

urlpatterns = [
    path(
        "",
        ClassAttendanceListCreate.as_view(),
        name="class-attendance-list-create",
    ),
    path(
        "<uuid:uid>/",
        ClassAttendanceDetail.as_view(),
        name="class-attendance-detail",
    ),
]
