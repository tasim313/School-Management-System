"""URLs for the SchoolAdminApp REST API."""

from django.urls import include, path


urlpatterns = [
    path(
        "libraries/",
        include("SchoolAdminApp.rest.urls.library"),
    ),
    path(
        "transports/",
        include("SchoolAdminApp.rest.urls.transport"),
    ),
    path(
        "hostels/",
        include("SchoolAdminApp.rest.urls.hostel"),
    ),
    path(
        "sports/",
        include("SchoolAdminApp.rest.urls.sports_information"),
    ),
    path(
        "department/",
        include("SchoolAdminApp.rest.urls.department"),
    ),
]
