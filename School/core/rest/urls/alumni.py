from django.urls import path

from core.rest.views.alumni import (
    AlumniSectionListCreateView,
    AlumniSectionRetrieveUpdateDeleteView,
    AlumniSectionImageListCreateView,
    AlumniSectionImageRetrieveUpdateDeleteView
)

urlpatterns = [
    path(
        "<slug:school_slug>/",
        AlumniSectionListCreateView.as_view(),
        name="alumni_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/",
        AlumniSectionRetrieveUpdateDeleteView.as_view(),
        name="alumni_delete",
    ),
    path(
        "<slug:school_slug>/image/",
        AlumniSectionImageListCreateView.as_view(),
        name="alumni_image_create"
    ),
    path(
        "<slug:school_slug>/<uuid:uid>/image/",
        AlumniSectionImageRetrieveUpdateDeleteView.as_view(),
        name="alumni_image_delete",
    ),
]
