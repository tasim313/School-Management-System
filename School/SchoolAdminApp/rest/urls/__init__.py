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
]
