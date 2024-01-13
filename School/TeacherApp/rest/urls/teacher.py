from django.urls import path
from TeacherApp.rest.views.teacher import TeacherListCreateAPIView, TeacherDetailView

urlpatterns = [
    path(
        "",
        TeacherListCreateAPIView.as_view(),
        name="teacher-list-create",
    ),
    path(
        "<uuid:uid>/",
        TeacherDetailView.as_view(),
        name="teacher-detail",
    ),
]
