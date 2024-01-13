from django.urls import path, include

urlpatterns = [
    path("/", include("TeacherApp.rest.urls.teacher")),
]
