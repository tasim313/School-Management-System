from django.urls import path, include

urlpatterns = [
     path("website/", include("core.rest.urls")),
     path("api/v1/core/", include("core.rest.urls")),
]
