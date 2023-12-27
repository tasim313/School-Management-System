from django.urls import include, path


urlpatterns = [
    path(
        "information/",
        include("StudentApp.rest.urls.student"),
    ),
]