from django.urls import path, include

urlpatterns = [
     path("website/", include("core.rest.urls")),
]