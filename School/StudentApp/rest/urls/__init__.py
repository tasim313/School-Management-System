from django.urls import include, path


urlpatterns = [
    path(
        "",
        include("StudentApp.rest.urls.student"),
    ),
]
