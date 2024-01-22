from django.urls import path
from core.rest.views.schoolClass import SchoolClassAPIView, SchoolClassListView, SchoolClassUpdateAPIView, SchoolClassDestroy

urlpatterns = [
    path(
        "",
        SchoolClassAPIView.as_view(),
        name="school-class-create",
    ),
    path(
        "<uuid:uid>/",
        SchoolClassUpdateAPIView.as_view(),
        name="school-class-update",
    ),
    path(
        "<slug:school_slug>/",
        SchoolClassListView.as_view(),
        name="school-class-list",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        SchoolClassDestroy.as_view(),
        name="school-class-delete",
    ),
]