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
        "class-time-tables/",
        include("SchoolAdminApp.rest.urls.class_time_table"),
    ),

    path(
        "department/",
        include("SchoolAdminApp.rest.urls.department"),
    ),

    path(
        "exams/",
        include("SchoolAdminApp.rest.urls.exam"),
    ),

    path(
        "subject/",
        include("SchoolAdminApp.rest.urls.subject"),

    ),
    
]
