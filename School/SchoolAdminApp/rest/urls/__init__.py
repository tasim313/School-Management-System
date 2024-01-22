from django.urls import include, path


urlpatterns = [
    path(
        "libraries/",
        include("SchoolAdminApp.rest.urls.library"),
    ),
    path(
        "hostels/",
        include("SchoolAdminApp.rest.urls.hostel"),
    ),
]
