from django.urls import path, include

urlpatterns = [
     path("api/", include("school_auth.rest.urls")),
]