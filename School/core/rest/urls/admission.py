from django.urls import path
from core.rest.views import admission

urlpatterns = [
    path(
        "",
        admission.AdmissionInformationAPIView.as_view(),
        name="school-admission-create",
    ),
    path(
        "<uuid:uid>/",
        admission.AdmissionInformationUpdateAPIView.as_view(),
        name="school-admission-update",
    ),
    path(
        "<slug:school_slug>/",
        admission.AdmissionInformationListView.as_view(),
        name="school-admission-list",
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        admission.AdmissionInformationDestroy.as_view(),
        name="school-admission-delete",
    ),
    path(
        "<slug:school_slug>/details/<uuid:uid>/",
        admission.AdmissionInformationDetailsListView.as_view(),
        name="school-admission-list",
    ),
]
