from django.urls import path
from core.rest.views import academic

urlpatterns = [
    path(
        "",
        academic.AcademicInformationList.as_view(),
        name="school-admission-list-create",
    ),
    path(
        "<uuid:uid>/",
        academic.AcademicInformationDetail.as_view(),
        name="school-admission-detail",
    ),
]
