from django.urls import path, include

urlpatterns = [
     path("api/student/", include("StudentApp.rest.urls")),
]