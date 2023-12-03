from django.urls import path, include

urlpatterns = [
     path("registration/", include("school_auth.rest.urls")),
]