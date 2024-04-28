from django.urls import include, path


urlpatterns = [
    path(
        "",
        include("StudentApp.rest.urls.student"),
    ),
     path(
        "status/",
        include("StudentApp.rest.urls.student_current_status.py"),
    ),
]
