from django.urls import path
from TeacherApp.rest.views.teacher import TeacherListCreateAPIView, TeacherDetailView, TeacherImageListCreateAPIView, TeacherImageDetailView

urlpatterns = [
    path(
        "<slug:school_slug>/",
        TeacherListCreateAPIView.as_view(),
        name="teacher-list-create",
    ),
    path(
        "<uuid:uid>/",
        TeacherDetailView.as_view(),
        name="teacher-detail",
    ),
    path(
        "image/",
        TeacherImageListCreateAPIView.as_view(),
        name="teacher-image-list-create",
    ),
    path(
        "image/<uuid:uid>/",
        TeacherImageDetailView.as_view(),
        name="teacher-image-detail",
    ),
]
