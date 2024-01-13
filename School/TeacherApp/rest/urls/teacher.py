from django.urls import path
from TeacherApp.rest.views.teacher import TeacherListCreateAPIView

urlpatterns = [
    path(
        "",
        TeacherListCreateAPIView.as_view(),
        name="teacher-list-create",
    ),
]
