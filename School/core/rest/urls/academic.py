from django.urls import path
from core.rest.views import academic

urlpatterns = [
    path(
        "",
        academic.AcademicInformationAPIView.as_view(),
        name="school-academic-create",
    ),
    path(
        "<uuid:uid>/",
        academic.AcademicInformationUpdateAPIView.as_view(),
        name="school-academic-update",
    ),
    path(
        "<slug:school_slug>/",
        academic.AcademicInformationListView.as_view(),
        name="school-academic-list",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        academic.AcademicInformationDestroy.as_view(),
        name="school-academic-delete",
    ),
    path(
        "<slug:school_slug>/details/<uuid:uid>/",
        academic.AcademicInformationDetailsListView.as_view(),
        name="school-academic-list",
    ),

]
