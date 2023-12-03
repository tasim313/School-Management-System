from django.urls import path, include

urlpatterns = [
     path("common/", include("common.rest.urls")),
]